from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, StudentRegisterForm, InstructorRegisterForm, ProfileRegisterForm
from django.contrib.auth.models import User
from .models import Student, Instructor
from school.models import EnrolledIn, AssistsIn, Course

def register(request):
    if not (request.user.is_authenticated):
        return redirect('login')
    if not (request.user.is_superuser):
        return redirect('access-denied')

    return render(request, 'users/register.html')


def register_student(request):
    if not (request.user.is_authenticated):
        return redirect('login')
    if not (request.user.is_superuser):
        return redirect('access-denied')

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


def profile(request, **kwargs):
    if not (request.user.is_authenticated):
        return redirect('login')

    user = request.user
    profile_user = User.objects.filter(username=kwargs.get('username')).first()

    # Profile does not exist
    if not profile_user:
        return redirect('access-denied')

    # Superusers can view anyone's profile
    if user.is_superuser:
        return render(request, 'users/profile.html', context={'kwargs': kwargs, 'profile_user': profile_user})

    # Users cannot view superuser's profile
    if (profile_user.is_superuser):
        return redirect('access-denied')

    # Anyone can view their own profile
    if (user == profile_user):
        return render(request, 'users/profile.html', context={'kwargs': kwargs, 'profile_user': profile_user})

    # Anyone can view an instructor's profile
    if Instructor.objects.filter(user=profile_user).exists():
        return render(request, 'users/profile.html', context={'kwargs': kwargs, 'profile_user': profile_user})

    # Students cannot view other students' profile
    student = Student.objects.filter(user=user).first()
    if student:
        return redirect('access-denied')

    # Instructors can view profiles of students they teach
    instructor = Instructor.objects.filter(user=user).first()
    if instructor:
        profile_student = Student.objects.filter(user=profile_user).first()
        student_enrollments = EnrolledIn.objects.filter(student=profile_student).values('course')
        student_assists = AssistsIn.objects.filter(student=profile_student).values('course')
        student_courses = student_enrollments.union(student_assists)
        student_instructors = Course.objects.filter(id__in=student_courses).values('instructor')
        print(student_instructors)
        if Instructor.objects.filter(user=instructor.user, user__in=student_instructors).exists():
            return render(request, 'users/profile.html', context={'kwargs': kwargs, 'profile_user': profile_user})

    return redirect('access-denied')


def access_denied(request):
    return render(request, 'users/access_denied.html')