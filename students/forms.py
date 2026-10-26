
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "name",
            "email",
            "phone",
            "course",
            "age",
            "city",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter student name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email address",
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter phone number",
            }),
            "course": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter course",
            }),
            "age": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter age",
            }),
            "city": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter city",
            }),
        }