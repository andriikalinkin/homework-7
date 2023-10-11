from django.http import HttpResponse
from django.shortcuts import render

from school.forms import TeacherForm


def index(request):
    return HttpResponse("<h1>Homework-6 index page</h1>")


def teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            # INSERT INTO DB
            return HttpResponse("<h1>You just add a teacher!</h1>")
    else:  # Render the form
        form = TeacherForm()

    return render(request, "teacher_form.html", {"form": form})


def teachers(request):
    return HttpResponse('<h1>"teachers/" page</h1>')


def group(request):
    return HttpResponse('<h1>"group/" page</h1>')


def groups(request):
    return HttpResponse('<h1>"groups/" page</h1>')
