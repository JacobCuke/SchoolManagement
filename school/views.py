from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class DashboardListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
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
    
    def test_func(self):
        dashboard_user = self.kwargs.get('username')
        if (self.request.user.username == dashboard_user):
            return True
        return False

    def handle_no_permission(self):
        return redirect('access-denied')
