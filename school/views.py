from django.http import HttpResponse
from django.shortcuts import render

# from app.models import <ClassModelName>


def index(request):
    return HttpResponse("Homework-6 index page")


def teacher(request):
    return HttpResponse("\"teacher/\" page")


def teachers(request):
    return HttpResponse("\"teachers/\" page")


def group(request):
    return HttpResponse("\"group/\" page")


def groups(request):
    return HttpResponse("\"groups/\" page")
