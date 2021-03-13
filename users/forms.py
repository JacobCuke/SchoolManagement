from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class StudentRegisterForm(forms.ModelForm):
    student_id_no = forms.IntegerField(min_value=0, max_value=99999999, label="Student ID Number")

    class Meta:
        model = Student
        fields = ['student_id_no', 'year']