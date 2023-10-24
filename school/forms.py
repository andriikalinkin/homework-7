import re

from django import forms

from .models import Teacher, Group


class TeacherForm(forms.Form):
    first_name = forms.CharField(
        label="First name:",
        widget=forms.TextInput(attrs={"placeholder": "Name"}),
    )

    last_name = forms.CharField(
        label="Last name:",
        widget=forms.TextInput(attrs={"placeholder": "Surname"}),
    )

    birthdate = forms.DateField(
        label="Birthdate:", widget=forms.TextInput(attrs={"placeholder": "YYYY-MM-DD"})
    )

    subject = forms.CharField(
        label="Subject:",
        widget=forms.TextInput(attrs={"placeholder": "Subject"}),
    )

    def clean(self):
        """Checking that `first_name`, `last_name`, subject` length under 51 characters."""
        cleaned_data = super().clean()

        first_name = cleaned_data.get("first_name")
        if len(first_name) > 50:
            raise forms.ValidationError("Name should be 50 characters or less.")

        last_name = cleaned_data.get("last_name")
        if len(last_name) > 50:
            raise forms.ValidationError("Surname should be 50 characters or less.")

        # birthdate = cleaned_data.get("birthdate")
        # if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(birthdate)):
        #     raise forms.ValidationError("Birthdate should be in the format YYYY-MM-DD.")

        subject = cleaned_data.get("subject")
        if len(subject) > 50:
            raise forms.ValidationError("Subject should be 50 characters or less.")

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
