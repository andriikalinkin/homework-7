from django.urls import path

from . import views

urlpatterns = [
    path("teacher_add/", views.teacher_add, name="teacher add"),
    path("teacher_edit/<int:pk>", views.teacher_edit, name="teacher edit"),
    path("teacher_delete/", views.teacher_delete, name="teacher delete"),
    path("teachers/", views.teachers, name="teachers"),
    path("group_add/", views.group_add, name="group add"),
    path("groups/", views.groups, name="groups"),
    path("student_add/", views.student_add, name="student add"),
    path("student_edit/<int:pk>", views.student_edit, name="student edit"),
    path("student_delete/", views.student_delete, name="student delete"),
    path("students/", views.students, name="students"),
]
