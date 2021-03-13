from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, StudentRegisterForm, ProfileRegisterForm
from django.contrib.auth.models import User

def register(request):
    return render(request, 'users/register.html')

def register_student(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST, prefix='user')
        student_form = StudentRegisterForm(request.POST, prefix='student')
        profile_form = ProfileRegisterForm(request.POST, prefix='profile')
        if (user_form.is_valid()):
            user = user_form.save()
            if (student_form.is_valid() and profile_form.is_valid()):
                student_form.instance.user = user
                student_form.save()
                user.profile.birth_date = profile_form.cleaned_data.get('birth_date')
                user.profile.address = profile_form.cleaned_data.get('address')
                user.save()
                messages.success(request, f'Account: {user.username} has been successfully created!')
                return redirect('login')
    else:
        context = {
            'user_form': UserRegisterForm(prefix='user'),
            'student_form': StudentRegisterForm(prefix='student'),
            'profile_form': ProfileRegisterForm(prefix='profile')
        }

    return render(request, 'users/register_student.html', context)
