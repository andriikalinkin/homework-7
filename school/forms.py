from django import forms


class TeacherForm(forms.Form):
    first_name = forms.CharField(
        label="First name:",
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder": "Name"}),
    )
    second_name = forms.CharField(
        label="Last name:",
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder": "Surname"}),
    )
    birthdate = forms.DateField(
        label="Birthdate:", widget=forms.TextInput(attrs={"placeholder": "YYYY-MM-DD"})
    )
    subject = forms.CharField(
        label="Subject:",
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Subject"}),
    )

    def clean(self):
        """Валидация форм.

        Данная функция должна сделать проверку форм first_name, second_name и subject на то что в них не более
        50-ти знаков, а в форме birthdate указан правильный формат даты в виде YYYY-MM-DD.
        """
