from django.http import HttpResponse
from django.shortcuts import render

# from app.models import <ClassModelName>


def index(request):
    return HttpResponse("<h1>Homework-6 index page</h1>")


def teacher(request):
    return HttpResponse("<h1>\"teacher/\" page</h1>")


def teachers(request):
    return HttpResponse("<h1>\"teachers/\" page</h1>")


def group(request):
    return HttpResponse("<h1>\"group/\" page</h1>")


def groups(request):
    return HttpResponse("<h1>\"groups/\" page</h1>")
