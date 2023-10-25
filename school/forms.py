import re

from django import forms

from .models import Teacher, Group, Student


class TeacherAddForm(forms.Form):
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")
    birthdate = forms.CharField(label="Birthday")
    subject = forms.CharField(label="Subject")

    def clean_birthday(self):
        cleaned_data = self.cleaned_data.get("birthdate")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(cleaned_data)):
            raise forms.ValidationError("Birthdate should be in the format \"YYYY-MM-DD\".")
        return cleaned_data

    def clean(self):
        cleaned_data = super().clean()

        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        subject = cleaned_data.get("subject")

        if len(first_name) > 50 or len(last_name) > 50 or len(subject) > 50:
            raise forms.ValidationError("First name, last name and subject must be 50 characters or less.")

        return cleaned_data


class TeacherEditForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "birthdate", "subject"]

    delete_teacher = forms.BooleanField(
        required=False, initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'delete-checkbox'}),
    )

    def clean(self):
        cleaned_data = super().clean()

        first_name = cleaned_data.get("first_name")
        if len(first_name) > 50:
            raise forms.ValidationError("First name should be 50 characters or less.")

        last_name = cleaned_data.get("last_name")
        if len(last_name) > 10:
            raise forms.ValidationError("Last name should be 50 characters or less.")

        subject = cleaned_data.get("subject")
        if len(subject) > 50:
            raise forms.ValidationError("Subject should be 50 characters or less.")

        return cleaned_data


class GroupForm(forms.Form):
    name = forms.CharField(label="Name:")
    curator = forms.ModelChoiceField(label="Curator:", queryset=Teacher.objects.all())

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get("name")
        if len(name) > 50:
            raise forms.ValidationError("Name should be 50 characters or less.")
        if name in Group.objects.values_list("name", flat=True):
            raise forms.ValidationError("This group already exists.")

        return cleaned_data


class StudentAddForm(forms.Form):
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")
    group = forms.ModelChoiceField(label="Group", queryset=Group.objects.all())

    def clean(self):
        cleaned_data = super().clean()

        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if len(first_name) > 50 or len(last_name) > 50:
            raise forms.ValidationError("First name and last name must be 50 characters or less.")

        return cleaned_data


class StudentEditForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "groups"]

    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        label="Groups",
        required=False
    )

    delete_student = forms.BooleanField(
        required=False, initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'delete-checkbox'}),
    )

    def clean(self):
        cleaned_data = super().clean()

        first_name = cleaned_data.get("first_name")
        if len(first_name) > 50:
            raise forms.ValidationError("First name should be 50 characters or less.")

        last_name = cleaned_data.get("last_name")
        if len(last_name) > 10:
            raise forms.ValidationError("Last name should be 50 characters or less.")

        return cleaned_data
