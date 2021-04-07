from django.urls import path
from . import views
from .views import (
    DashboardListView,
    CourseDetailView,
    ExtraCurricularCreateView,
    ExtraCurricularUpdateView,
    ExtraCurricularDeleteView,
    GuardianCreateView,
    GuardianUpdateView,
    GuardianDeleteView,
    LectureListView,
    LectureDetailView,
    AssignmentListView,
    AssignmentDetailView,
    SubmissionCreateView,
    LectureCreateView,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<str:username>/', DashboardListView.as_view(), name='user-dashboard'),
    path('course/<int:pk>/', views.course, name='course-detail'),
    path('course/<int:course_id>/lectures/', LectureListView.as_view(), name='lecture-list'),
    path('course/<int:course_id>/lectures/new/', LectureCreateView.as_view(), name='create-lecture'),
    path('course/<int:course_id>/lectures/<int:pk>/', LectureDetailView.as_view(), name='lecture-detail'),
    path('course/<int:course_id>/assignments/', AssignmentListView.as_view(), name='assignment-list'),
    path('course/<int:course_id>/assignments/<int:pk>/', AssignmentDetailView.as_view(), name='assignment-detail'),
    path('course/<int:course_id>/assignments/<int:pk>/submit/', SubmissionCreateView.as_view(), name='add-submission'),
    path('extracurricular/new/', ExtraCurricularCreateView.as_view(), name='create-extra-curricular'),
    path('extracurricular/<int:pk>/update/', ExtraCurricularUpdateView.as_view(), name='update-extra-curricular'),
    path('extracurricular/<int:pk>/delete/', ExtraCurricularDeleteView.as_view(), name='delete-extra-curricular'),
    path('guardian/new/', GuardianCreateView.as_view(), name='create-guardian'),
    path('guardian/<int:pk>/update/', GuardianUpdateView.as_view(), name='update-guardian'),
    path('guardian/<int:pk>/delete/', GuardianDeleteView.as_view(), name='delete-guardian')
]