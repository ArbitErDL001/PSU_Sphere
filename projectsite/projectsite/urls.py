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
from studentorg.views import dashboard, delete_entity, home, manage_entity

urlpatterns = [
    path('', home, name='home'),
    path('index.html', dashboard, name='index'),
    path('students/', lambda request: manage_entity(request, 'students'), name='student-list'),
    path('students/<int:pk>/delete/', lambda request, pk: delete_entity(request, 'students', pk), name='student-delete'),
    path('members/', lambda request: manage_entity(request, 'members'), name='member-list'),
    path('members/<int:pk>/delete/', lambda request, pk: delete_entity(request, 'members', pk), name='member-delete'),
    path('organizations/', lambda request: manage_entity(request, 'organizations'), name='organization-list'),
    path('organizations/<int:pk>/delete/', lambda request, pk: delete_entity(request, 'organizations', pk), name='organization-delete'),
    path('programs/', lambda request: manage_entity(request, 'programs'), name='program-list'),
    path('programs/<int:pk>/delete/', lambda request, pk: delete_entity(request, 'programs', pk), name='program-delete'),
    path('colleges/', lambda request: manage_entity(request, 'colleges'), name='college-list'),
    path('colleges/<int:pk>/delete/', lambda request, pk: delete_entity(request, 'colleges', pk), name='college-delete'),
    path('components.html', lambda request: manage_entity(request, 'students'), name='components'),
    path('forms.html', lambda request: manage_entity(request, 'members'), name='forms'),
    path('tables.html', lambda request: manage_entity(request, 'organizations'), name='tables'),
    path('notifications.html', lambda request: manage_entity(request, 'programs'), name='notifications'),
    path('typography.html', lambda request: manage_entity(request, 'colleges'), name='typography'),
    path('icons.html', dashboard, name='icons'),
    path('admin/', admin.site.urls),
]
