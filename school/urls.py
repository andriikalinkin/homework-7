from django.urls import path

from . import views

urlpatterns = [
    path("teacher_add/", views.teacher_add, name="teacher_add"),
    path("teachers/", views.teachers, name="teachers"),
    path("group_add/", views.group_add, name="group_add"),
    path("groups/", views.groups, name="groups"),
]
