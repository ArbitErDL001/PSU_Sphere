from django import forms

from .models import College, OrgMember, Organization, Program, Student


class StyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")


class CollegeForm(StyledModelForm):
    class Meta:
        model = College
        fields = ("college_name",)
        labels = {"college_name": "College name"}


class ProgramForm(StyledModelForm):
    class Meta:
        model = Program
        fields = ("prog_name", "college")
        labels = {"prog_name": "Program name"}


class OrganizationForm(StyledModelForm):
    class Meta:
        model = Organization
        fields = ("name", "college", "description")
        widgets = {"description": forms.Textarea(attrs={"rows": 3})}


class StudentForm(StyledModelForm):
    class Meta:
        model = Student
        fields = ("student_id", "lastname", "firstname", "middlename", "program")
        labels = {
            "student_id": "Student ID",
            "lastname": "Last name",
            "firstname": "First name",
            "middlename": "Middle name",
        }


class OrgMemberForm(StyledModelForm):
    class Meta:
        model = OrgMember
        fields = ("student", "organization", "date_joined")
        labels = {"date_joined": "Date joined"}
        widgets = {"date_joined": forms.DateInput(attrs={"type": "date"})}
