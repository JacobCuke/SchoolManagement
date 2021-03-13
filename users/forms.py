from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Profile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class StudentRegisterForm(forms.ModelForm):
    student_id_no = forms.IntegerField(min_value=0, max_value=99999999, label="Student ID Number")

    class Meta:
        model = Student
        fields = ['student_id_no', 'year']


class ProfileRegisterForm(forms.ModelForm):
    birth_date = forms.DateField(
                                    widget=forms.DateInput(attrs={'autocomplete':'off', 'class': 'date-picker'}, 
                                    format='%Y/%m/%d'),
                                    input_formats=['%Y/%m/%d'],
                                    required=False
                                )

    class Meta:
        model = Profile
        fields = ['birth_date', 'address']