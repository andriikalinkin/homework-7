from django.shortcuts import render, redirect

from .forms import TeacherAddEditForm, TeacherDeleteForm, GroupForm, StudentAddEditForm, StudentDeleteForm
from .models import Teacher, Group, Student


def teacher_add(request):
    if request.method == "POST":
        form = TeacherAddEditForm(request.POST)
        if form.is_valid():
            teacher_create = Teacher.objects.create(
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                birthdate=request.POST["birthdate"],
                subject=request.POST["subject"],
            )
            teacher_create.save()
            return redirect("students")
        return render(request, "teacher_add.html", {"form": form})
    form = TeacherAddEditForm()
    return render(request, "teacher_add.html", {"form": form})


def teacher_edit(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == "GET":
        form = TeacherAddEditForm(instance=teacher)
        return render(request, "teacher_edit.html", {"form": form})
    form = TeacherAddEditForm(request.POST, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect("teachers")
    return render(request, "teacher_edit.html", {"form": form})


def teacher_delete(request):
    if request.method == "POST":
        form = TeacherDeleteForm(request.POST)
        if form.is_valid():
            teacher = Teacher.objects.get(pk=request.POST["teacher_id"])
            teacher.delete()
            return redirect("teachers")
        return render(request, "teacher_delete.html", {"form": form})
    form = TeacherDeleteForm()
    return render(request, "teacher_delete.html", {"form": form})


def teachers(request):
    all_teachers = Teacher.objects.all()
    return render(request, "teachers.html", {"all_teachers": all_teachers})


def group_add(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group_create = Group.objects.create(
                name=request.POST["name"],
                curator=form.cleaned_data["curator"]
            )
            group_create.save()
            return redirect("/groups/")
        return render(request, "group.html", {"form": form})
    form = GroupForm()
    return render(request, "group.html", {"form": form})


def groups(request):
    all_groups = Group.objects.all()
    return render(request, "groups.html", {"all_groups": all_groups})


def student_add(request):
    if request.method == "POST":
        form = StudentAddEditForm(request.POST)
        if form.is_valid():
            student_create = Student.objects.create(
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
            )
            student_create.save()
            return redirect("students")
        return render(request, "student_add.html", {"form": form})
    form = TeacherAddEditForm()
    return render(request, "student_add.html", {"form": form})


def student_edit(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == "GET":
        form = StudentAddEditForm(instance=student)
        return render(request, "student_edit.html", {"form": form})
    form = StudentAddEditForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect("students")
    return render(request, "student_edit.html", {"form": form})


def student_delete(request):
    if request.method == "POST":
        form = StudentDeleteForm(request.POST)
        if form.is_valid():
            student = Student.objects.get(pk=request.POST["student_id"])
            student.delete()
            return redirect("students")
        return render(request, "student_delete.html", {"form": form})
    form = StudentDeleteForm()
    return render(request, "student_delete.html", {"form": form})


def students(request):
    all_students = Student.objects.all()
    return render(request, "students.html", {"all_students": all_students})
