from django.shortcuts import render
from django.views.generic.list import ListView
from studentorg.models import Organization

# Create your views here.

class HomePageView(ListView):
    model = Organization
    context_object_name = 'organizations'
    template_name = "home.html"
    paginate_by = 10

