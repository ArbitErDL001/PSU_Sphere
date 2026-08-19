"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from studentorg.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('index.html', TemplateView.as_view(template_name='index.html'), name='index'),
    path('components.html', TemplateView.as_view(template_name='components.html'), name='components'),
    path('forms.html', TemplateView.as_view(template_name='forms.html'), name='forms'),
    path('tables.html', TemplateView.as_view(template_name='tables.html'), name='tables'),
    path('notifications.html', TemplateView.as_view(template_name='notifications.html'), name='notifications'),
    path('typography.html', TemplateView.as_view(template_name='typography.html'), name='typography'),
    path('icons.html', TemplateView.as_view(template_name='icons.html'), name='icons'),
    path('admin/', admin.site.urls),
]
