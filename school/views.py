from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Course, EnrolledIn, AssistsIn
from users.models import Student
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def home(request) :
    if (request.user.is_authenticated):
        return redirect('user-dashboard', username=request.user.username)
    else:
        return render(request, 'school/home.html')


def dashboard(request):
    if (request.user.is_authenticated):
        return redirect('user-dashboard', username=request.user.username)
    else:
        return render(request, 'login')


class DashboardListView(ListView):
    model = Course
    template_name = 'school/dashboard.html'
    context_object_name = 'courses'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        queryset = {}

        student = Student.objects.filter(user=user).first()
        if student:
            enrollments = EnrolledIn.objects.filter(student=student).values('course')
            queryset['enrolled_courses'] = Course.objects.filter(id__in=enrollments)

            assists = AssistsIn.objects.filter(student=student).values('course')
            queryset['assisted_courses'] = Course.objects.filter(id__in=assists)

        return queryset
