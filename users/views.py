from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, StudentRegisterForm, InstructorRegisterForm, ProfileRegisterForm
from django.contrib.auth.models import User

def register(request):
    if not (request.user.is_authenticated):
        return redirect('login')
    if not (request.user.is_superuser):
        return redirect('access-denied')

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


def register_instructor(request):
    if not (request.user.is_authenticated):
        return redirect('login')
    if not (request.user.is_superuser):
        return redirect('access-denied')

    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST, prefix='user')
        instructor_form = InstructorRegisterForm(request.POST, prefix='instructor')
        profile_form = ProfileRegisterForm(request.POST, prefix='profile')
        if (user_form.is_valid()):
            user = user_form.save()
            if (instructor_form.is_valid() and profile_form.is_valid()):
                instructor_form.instance.user = user
                instructor_form.save()
                user.profile.birth_date = profile_form.cleaned_data.get('birth_date')
                user.profile.address = profile_form.cleaned_data.get('address')
                user.save()
                messages.success(request, f'Account: {user.username} has been successfully created!')
                return redirect('login')
    else:
        context = {
            'user_form': UserRegisterForm(prefix='user'),
            'instructor_form': InstructorRegisterForm(prefix='instructor'),
            'profile_form': ProfileRegisterForm(prefix='profile')
        }

    return render(request, 'users/register_instructor.html', context)


def access_denied(request):
    return render(request, 'users/access_denied.html')