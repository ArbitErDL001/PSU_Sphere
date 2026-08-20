from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CollegeForm, OrgMemberForm, OrganizationForm, ProgramForm, StudentForm
from .models import College, OrgMember, Organization, Program, Student


def dashboard(request):
    context = {
        "student_count": Student.objects.count(),
        "member_count": OrgMember.objects.count(),
        "organization_count": Organization.objects.count(),
        "program_count": Program.objects.count(),
        "college_count": College.objects.count(),
        "organizations": Organization.objects.annotate(member_count=Count("orgmember")).order_by("name")[:5],
        "recent_students": Student.objects.select_related("program").order_by("-created_at")[:5],
    }
    return render(request, "index.html", context)


def home(request):
    return redirect("index")


ENTITY_CONFIG = {
    "students": (Student, StudentForm, "Students", "student_id", "student-list", "student-delete"),
    "members": (OrgMember, OrgMemberForm, "Org members", "student", "member-list", "member-delete"),
    "organizations": (Organization, OrganizationForm, "Organizations", "name", "organization-list", "organization-delete"),
    "programs": (Program, ProgramForm, "Programs", "prog_name", "program-list", "program-delete"),
    "colleges": (College, CollegeForm, "Colleges", "college_name", "college-list", "college-delete"),
}


def manage_entity(request, entity):
    model, form_class, title, order_field, route_name, delete_route = ENTITY_CONFIG[entity]
    form = form_class(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"{title[:-1] if title.endswith('s') else title} added successfully.")
        return redirect(route_name)
    query = request.GET.get("q", "").strip()
    objects = model.objects.all()
    search_fields = {
        "students": ("student_id", "lastname", "firstname", "middlename", "program__prog_name"),
        "members": ("student__student_id", "student__lastname", "student__firstname", "organization__name"),
        "organizations": ("name", "description", "college__college_name"),
        "programs": ("prog_name", "college__college_name"),
        "colleges": ("college_name",),
    }[entity]
    if query:
        search_query = Q()
        for field in search_fields:
            search_query |= Q(**{f"{field}__icontains": query})
        objects = objects.filter(search_query)
    objects = objects.order_by(order_field)
    if entity == "members":
        objects = objects.select_related("student", "organization")
    elif entity == "students":
        objects = objects.select_related("program", "program__college")
    elif entity == "programs":
        objects = objects.select_related("college")
    elif entity == "organizations":
        objects = objects.select_related("college")
    return render(request, "manage.html", {
        "title": title,
        "entity": entity,
        "form": form,
        "objects": objects,
        "route_name": route_name,
        "delete_route": delete_route,
        "query": query,
    })


def delete_entity(request, entity, pk):
    model, _, title, _, route_name, _ = ENTITY_CONFIG[entity]
    if request.method == "POST":
        item = get_object_or_404(model, pk=pk)
        item.delete()
        messages.success(request, f"{title[:-1] if title.endswith('s') else title} deleted.")
    return redirect(route_name)

