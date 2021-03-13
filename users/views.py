from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, StudentRegisterForm

def register(request):
    return render(request, 'users/register.html')

def register_student(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        student_form = StudentRegisterForm(request.POST)
        if (user_form.is_valid() and student_form.is_valid()):
            user_form.save()
            student_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account: {username} has been successfully created!')
            return redirect('login')
    else:
        context = {
            'user_form': UserRegisterForm(),
            'student_form': StudentRegisterForm()
        }

    return render(request, 'users/register_student.html', context)
