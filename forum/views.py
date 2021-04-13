from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ThreadForm, PostForm
from school.models import Course, EnrolledIn, AssistsIn
from users.models import Student, Instructor

@login_required
def create_thread(request, **kwargs):

    user = request.user
    course = get_object_or_404(Course, id=kwargs.get('course_id'))

    # Students can post in courses they are enrolled in or assist in
    student = Student.objects.filter(user=user).first()
    if student:
        if not (EnrolledIn.objects.filter(student=student, course=course).exists() or AssistsIn.objects.filter(student=student, course=course).exists()):
            return redirect('access-denied')

    # Instructors can post in courses that they teach
    instructor = Instructor.objects.filter(user=user).first()
    if instructor:
        if course.instructor != instructor:
            return redirect('access-denied')

    if request.method == 'POST':
        thread_form = ThreadForm(request.POST, prefix='thread')
        post_form = PostForm(request.POST, prefix='post')
        if (thread_form.is_valid() and post_form.is_valid()):
            thread_form.instance.course = course
            thread_form.instance.author = request.user
            thread = thread_form.save()

            post_form.instance.thread = thread
            post_form.instance.author = request.user
            post_form.save()

            messages.success(request, f'Thread successfully created!')

            # NEEDS TO BE CHANGED TO NEWLY CREATED THREAD PAGE (POST LIST)
            return redirect('dashboard')

    else:
        view = {
            'kwargs': kwargs
        }

        context = {
            'thread_form': ThreadForm(prefix='thread'),
            'post_form': PostForm(prefix='post'),
            'view': view
        }
        return render(request, 'forum/create_thread.html', context)
