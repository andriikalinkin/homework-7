from django import forms

from .models import Teacher, Group


class TeacherAddEditForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "birthdate", "subject"]

    def clean(self):
        cleaned_data = super().clean()

        first_name = cleaned_data.get("first_name")
        if len(first_name) > 50:
            raise forms.ValidationError("Name should be 50 characters or less.")

        last_name = cleaned_data.get("last_name")
        if len(last_name) > 10:
            raise forms.ValidationError("Surname should be 50 characters or less.")

        subject = cleaned_data.get("subject")
        if len(subject) > 50:
            raise forms.ValidationError("Subject should be 50 characters or less.")

        return cleaned_data


class TeacherDeleteForm(forms.Form):
    teacher_id = forms.CharField(label="Teacher's ID:")

    def clean_teacher_id(self):
        cleaned_data = self.cleaned_data.get("teacher_id")
        if not cleaned_data.isdigit():
            raise forms.ValidationError("Use int() only.")
        if not Teacher.objects.filter(id=cleaned_data).exists():
            raise forms.ValidationError("Invalid ID.")
        return cleaned_data


class GroupForm(forms.Form):
    name = forms.CharField(
        label="Name:",
        widget=forms.TextInput(attrs={"placeholder": "Name"}),
    )

    curator = forms.ModelChoiceField(
        label="Curator:",
        queryset=Teacher.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get("name")
        if len(name) > 50:
            raise forms.ValidationError("Name should be 50 characters or less.")
        if name in Group.objects.values_list("name", flat=True):
            raise forms.ValidationError("This group already exists.")

        return cleaned_data
