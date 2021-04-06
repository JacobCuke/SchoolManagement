from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Course, EnrolledIn, AssistsIn, ExtraCurricular, Guardian, Lecture, Assignment
from .forms import ExtraCurricularForm, GuardianForm
from users.models import Student, Instructor
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse, Http404, HttpResponse, HttpResponseNotFound
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
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
        return redirect('login')

def course(request, **kwargs):
    if (request.user.is_authenticated):
        return redirect('lecture-list', course_id = kwargs.get('pk'))
    else:
        return redirect('login')

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

        instructor = Instructor.objects.filter(user=user).first()
        if instructor:
            queryset['taught_courses'] = Course.objects.filter(instructor=instructor)

        return queryset
    
    def test_func(self):
        dashboard_user = self.kwargs.get('username')
        if (self.request.user.username == dashboard_user):
            return True
        return False


class LectureListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Lecture
    template_name = 'school/lecture.html'
    context_object_name = 'lectures'

    def get_queryset(self):
        queryset = {}
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))
        

        queryset['lecture_list']= Lecture.objects.filter(course=course)
        queryset['course'] = course 
        return queryset
    
    
    def test_func(self):
        user = self.request.user
        student = Student.objects.filter(user=user).first()
        course = self.kwargs.get('course_id')

        if student:
            if EnrolledIn.objects.filter(student=student, course=course).exists():
                return True
            if AssistsIn.objects.filter(student=student, course=course).exists():
                return True
        
        instructor = Instructor.objects.filter(user=user).first()
        if instructor:
            if course.instructor == instructor:
                return True

        if user.is_superuser:
            return True
        return False

class LectureDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Lecture
    context_object_name = 'lecture'

    def pdf_view(request):
        with open('media\file_uploads\471-W21-Q2-sample_YCjX27B.pdf', 'rb') as pdf:
            response = HttpResponse(pdf.read(),content_type='application/pdf')
            response['Content-Disposition'] = 'filename=some_file.pdf'
            return response
             
    def test_func(self):
        user = self.request.user
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))

        student = Student.objects.filter(user=user).first()
        if student:
            if EnrolledIn.objects.filter(student=student, course=course).exists():
                return True
            if AssistsIn.objects.filter(student=student, course=course).exists():
                return True
        
        instructor = Instructor.objects.filter(user=user).first()
        if instructor:
            if course.instructor == instructor:
                return True

        if user.is_superuser:
            return True        
        return False
    
class AssignmentListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Assignment
    template_name = 'school/assignment.html'
    context_object_name = 'assignments'

    def get_queryset(self):
        queryset = {}
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))
        

        queryset['assignment_list']= Assignment.objects.filter(course=course)
        queryset['course'] = course 
        return queryset
    
    
    def test_func(self):
        user = self.request.user
        student = Student.objects.filter(user=user).first()
        course = self.kwargs.get('course_id')

        if student:
            if EnrolledIn.objects.filter(student=student, course=course).exists():
                return True
            if AssistsIn.objects.filter(student=student, course=course).exists():
                return True
        
        instructor = Instructor.objects.filter(user=user).first()
        if instructor:
            if course.instructor == instructor:
                return True

        if user.is_superuser:
            return True
        return False

class AssignmentDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Assignment
    context_object_name = 'assignment'

    def pdf_view(request):
        with open('media\file_uploads\471-W21-Q2-sample_YCjX27B.pdf', 'rb') as pdf:
            response = HttpResponse(pdf.read(),content_type='application/pdf')
            response['Content-Disposition'] = 'filename=some_file.pdf'
            return response
             
    def test_func(self):
        user = self.request.user
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))

        student = Student.objects.filter(user=user).first()
        if student:
            if EnrolledIn.objects.filter(student=student, course=course).exists():
                return True
            if AssistsIn.objects.filter(student=student, course=course).exists():
                return True
        
        instructor = Instructor.objects.filter(user=user).first()
        if instructor:
            if course.instructor == instructor:
                return True

        if user.is_superuser:
            return True        
        return False
    
class CourseDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Course

    def test_func(self):
        user = self.request.user
        course = self.get_object()

        student = Student.objects.filter(user=user).first()
        if student:
            if EnrolledIn.objects.filter(student=student, course=course).exists():
                return True
            if AssistsIn.objects.filter(student=student, course=course).exists():
                return True
        
        instructor = Instructor.objects.filter(user=user).first()
        if instructor:
            if course.instructor == instructor:
                return True

        return False

class ExtraCurricularCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = ExtraCurricularForm
    template_name = 'school/extra_curricular_form.html'
    is_student = False

    def form_valid(self, form):
        student = Student.objects.filter(user=self.request.user).first()
        form.instance.student = student
        return super().form_valid(form)

    # User must be a Student and can only have a max of 5 activities
    def test_func(self):
        user = self.request.user
        student = Student.objects.filter(user=user).first()
        if student:
            self.is_student = True
            if (ExtraCurricular.objects.filter(student=student).count() >= 5):
                return False
            return True
        else:
            return False


    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            if self.is_student:
                return render(self.request, 'school/max_extra_curriculars.html')
            else:
                return redirect('access-denied')
        else:
            return redirect('login')


class ExtraCurricularUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ExtraCurricular
    form_class = ExtraCurricularForm
    template_name = 'school/extra_curricular_update_form.html'

    def form_valid(self, form):
        student = Student.objects.filter(user=self.request.user).first()
        form.instance.student = student
        return super().form_valid(form)
    
    def test_func(self):
        extra_curricular = self.get_object()
        student = Student.objects.filter(user=self.request.user).first()
        if student:
            if student == extra_curricular.student:
                return True
        return False


class ExtraCurricularDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ExtraCurricular
    success_url = '/profile/'
    template_name = 'school/extra_curricular_confirm_delete.html'
    
    def test_func(self):
        extra_curricular = self.get_object()
        student = Student.objects.filter(user=self.request.user).first()
        if student:
            if student == extra_curricular.student:
                return True
        return False


class GuardianCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = GuardianForm
    template_name = 'school/guardian_form.html'
    is_student = False

    def form_valid(self, form):
        student = Student.objects.filter(user=self.request.user).first()
        form.instance.student = student
        return super().form_valid(form)

    # User must be a Student and can only have a max of 2 guardians
    def test_func(self):
        user = self.request.user
        student = Student.objects.filter(user=user).first()
        if student:
            self.is_student = True
            if (Guardian.objects.filter(student=student).count() >= 2):
                return False
            return True
        else:
            return False

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            if self.is_student:
                return render(self.request, 'school/max_guardians.html')
            else:
                return redirect('access-denied')
        else:
            return redirect('login')


class GuardianUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Guardian
    form_class = GuardianForm
    template_name = 'school/guardian_update_form.html'

    def form_valid(self, form):
        student = Student.objects.filter(user=self.request.user).first()
        form.instance.student = student
        return super().form_valid(form)
    
    def test_func(self):
        guardian = self.get_object()
        student = Student.objects.filter(user=self.request.user).first()
        if student:
            if student == guardian.student:
                return True
        return False


class GuardianDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Guardian
    success_url = '/profile/'
    template_name = 'school/guardian_confirm_delete.html'
    
    def test_func(self):
        guardian = self.get_object()
        student = Student.objects.filter(user=self.request.user).first()
        if student:
            if student == guardian.student:
                return True
        return False