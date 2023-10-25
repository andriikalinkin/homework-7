from django.shortcuts import render, redirect, HttpResponse

from .forms import TeacherAddForm, TeacherEditForm, GroupForm, StudentAddForm, StudentEditForm
from .models import Teacher, Group, Student


def teacher_add(request):
    if request.method == "POST":
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            teacher_create = Teacher.objects.create(
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                birthdate=request.POST["birthdate"],
                subject=request.POST["subject"],
            )
            teacher_create.save()
            return redirect("teachers")
        return render(request, "teacher_add.html", {"form": form})
    form = TeacherAddForm()
    return render(request, "teacher_add.html", {"form": form})


def teacher_edit(request, pk=None):
    teacher = None

    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        pass

    if request.method == "GET":
        if pk:
            form = TeacherEditForm(instance=teacher)
            return render(request, "teacher_edit.html", {"form":form})
        return HttpResponse("<h1>To edit or delete a teacher use teacher_edit/teacher_id</h1>")
    form = TeacherEditForm(request.POST, instance=teacher)
    if "delete_teacher" in request.POST:
        teacher.delete()
        return redirect("teachers")
    if form.is_valid():
        form.save()
        return redirect("teachers")
    return render(request, "teacher_edit.html", {"form": form})


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
        form = StudentAddForm(request.POST)
        if form.is_valid():
            student_create = Student.objects.create(
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                group=request.POST["group"],
            )
            student_create.save()
            return redirect("students")
        return render(request, "student_add.html", {"form": form})
    form = StudentAddForm()
    return render(request, "student_add.html", {"form": form})


def student_edit(request, pk=None):
    student = None

    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        pass

    if request.method == "GET":
        if pk:
            form = StudentEditForm(instance=student)
            return render(request, "student_edit.html", {"form": form})
        return HttpResponse("<h1>To edit or delete a student use student_edit/student_id</h1>")
    form = StudentEditForm(request.POST, instance=student)
    if "delete_student" in request.POST:
        student.delete()
        return redirect("students")
    if form.is_valid():
        form.save()
        return redirect("students")
    return render(request, "student_edit.html", {"form": form})


def students(request):
    all_students = Student.objects.all()
    return render(request, "students.html", {"all_students": all_students})


def student_groups(request):
    all_student_groups = Student.objects.all()  # .values('groups')
    return render(request, "student_groups.html", {"all_student_groups": all_student_groups})
