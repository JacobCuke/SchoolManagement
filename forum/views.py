from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import ThreadForm, PostForm
from .models import DiscussionThread, DiscussionPost
from school.models import Course, EnrolledIn, AssistsIn
from users.models import Student, Instructor
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
)

class DiscussionThreadListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    # TO DO
    model = DiscussionThread
    template_name = 'forum/thread_list.html'
    context_object_name = 'threads'

    def get_queryset(self):
        queryset = {}
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))

        queryset['thread_list']= DiscussionThread.objects.filter(course=course).order_by('-creation_date_time')
        queryset['course'] = course
        return queryset

    def test_func(self):
        user = self.request.user
        student = Student.objects.filter(user=user).first()
        course_id = self.kwargs.get('course_id')
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))

        if student:
            if EnrolledIn.objects.filter(student=student, course=course_id).exists():
                return True
            if AssistsIn.objects.filter(student=student, course=course_id).exists():
                return True
        
        instructor = Instructor.objects.filter(user=user).first()
        if instructor:
            if course.instructor == instructor:
                return True

        if user.is_superuser:
            return True
        return False

class DiscussionPostListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    # TO DO
    model = DiscussionPost
    template_name = 'forum/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = {}
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))
        thread = get_object_or_404(DiscussionThread, id=self.kwargs.get('pk'), course=course)

        queryset['post_list']= DiscussionPost.objects.filter(thread=thread).order_by('creation_date_time')
        queryset['course'] = course 
        queryset['thread'] = thread
        return queryset

    def test_func(self):
        user = self.request.user
        student = Student.objects.filter(user=user).first()
        course_id = self.kwargs.get('course_id')
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))

        if student:
            if EnrolledIn.objects.filter(student=student, course=course_id).exists():
                return True
            if AssistsIn.objects.filter(student=student, course=course_id).exists():
                return True
        
        instructor = Instructor.objects.filter(user=user).first()
        if instructor:
            if course.instructor == instructor:
                return True

        if user.is_superuser:
            return True
        return False

class DiscussionPostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    # TO DO
    model = DiscussionPost
    fields = ['content']
    template_name = 'forum/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.thread = get_object_or_404(DiscussionThread, pk=self.kwargs.get('pk'), course=self.kwargs.get('course_id'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-list', kwargs={'course_id': self.kwargs.get('course_id'), 'pk': self.kwargs.get('pk')})

    def test_func(self):
        user = self.request.user
        student = Student.objects.filter(user=user).first()
        course_id = self.kwargs.get('course_id')
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))

        if student:
            if EnrolledIn.objects.filter(student=student, course=course_id).exists():
                return True
            if AssistsIn.objects.filter(student=student, course=course_id).exists():
                return True
        
        instructor = Instructor.objects.filter(user=user).first()
        if instructor:
            if course.instructor == instructor:
                return True

        if user.is_superuser:
            return True
        return False


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
            return redirect('thread-list', course_id=kwargs.get('course_id'))

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
