from django.urls import path

from . import views

urlpatterns = [
    path("teacher/", views.teacher, name="teacher"),
    path("teachers/", views.teachers, name="teachers"),
    path("group/", views.group, name="group"),
    path("groups/", views.groups, name="groups"),
]
