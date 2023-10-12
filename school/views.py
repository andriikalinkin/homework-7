from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TeacherForm
from .models import Teacher


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
    else:
        form = TeacherForm()

    return render(request, "teacher_form.html", {"form": form})


def teachers(request):
    all_teachers = Teacher.objects.all()
    return render(request, "teachers.html", {"all_teachers": all_teachers})


def group(request):
    return HttpResponse('<h1>"group/" page</h1>')


def groups(request):
    return HttpResponse('<h1>"groups/" page</h1>')
