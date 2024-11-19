from django import forms
from django.contrib.auth.hashers import make_password
from .models import Faculty  

class FacultyForm(forms.ModelForm):

    SUBJECT_CHOICES = [
        (1, 'Math'),
        (2, 'English'),
        (3, 'Science'),
        (4, 'History'),
        (5, 'Geography'),
        (6, 'Physics'),
        (7, 'Chemistry'),
        (8, 'Biology'),
        (9, 'Art'),
        (10, 'Physical Education')
    ]
    
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES, required=False)

    class Meta:

        model = Faculty

        fields = ['first_name', 'last_name', 'email', 'password', 'subject', 'phone_number']

    def save(self, commit=True):

        faculty = super().save(commit=False)

        if faculty.password:

            faculty.password = make_password(faculty.password)  

        if commit:

            faculty.save()

        return faculty


