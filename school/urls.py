from django.urls import path

from . import views

urlpatterns = [
    path("teacher_add/", views.teacher_add, name="teacher add"),
    path("teacher_edit/", views.teacher_edit, name="how to edit a teacher"),
    path("teacher_edit/<int:pk>", views.teacher_edit, name="teacher edit"),
    path("teachers/", views.teachers, name="teachers"),
    path("group_add/", views.group_add, name="group add"),
    path("groups/", views.groups, name="groups"),
    path("student_add/", views.student_add, name="student add"),
    path("student_edit/", views.teacher_edit, name="how to edit a student"),
    path("student_edit/<int:pk>", views.student_edit, name="student edit"),
    path("students/", views.students, name="students"),
    path("student_groups/", views.student_groups, name="student and groups"),
]
