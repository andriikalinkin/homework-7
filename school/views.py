from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TeacherForm, GroupForm
from .models import Teacher, Group


def index(request):
    return HttpResponse("<h1>Homework-6 index page</h1>")


def teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher_create = Teacher.objects.create(
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                birthdate=request.POST["birthdate"],
                subject=request.POST["subject"],
            )
            teacher_create.save()

            return redirect("/teachers/")

    form = TeacherForm()  # Verification form failed.

    return render(request, "teacher_form.html", {"form": form})


def teachers(request):
    all_teachers = Teacher.objects.all()

    return render(request, "teachers.html", {"all_teachers": all_teachers})


def group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group_create = Group.objects.create(
                name=request.POST["name"],
                curator=form.cleaned_data["curator"]
            )
            group_create.save()

            return redirect("/groups/")

    form = GroupForm()  # Verification form failed.

    return render(request, "group_form.html", {"form": form})


def groups(request):
    all_groups = Group.objects.all()

    return render(request, "groups.html", {"all_groups": all_groups})
