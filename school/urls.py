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
    LectureListView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<str:username>/', DashboardListView.as_view(), name='user-dashboard'),
    path('course/<int:pk>/', views.course, name='course-detail'),
    path('course/<int:course_id>/lectures/', LectureListView.as_view(), name='lecture-list'),
    path('extracurricular/new/', ExtraCurricularCreateView.as_view(), name='create-extra-curricular'),
    path('extracurricular/<int:pk>/update/', ExtraCurricularUpdateView.as_view(), name='update-extra-curricular'),
    path('extracurricular/<int:pk>/delete/', ExtraCurricularDeleteView.as_view(), name='delete-extra-curricular'),
    path('guardian/new/', GuardianCreateView.as_view(), name='create-guardian'),
    path('guardian/<int:pk>/update/', GuardianUpdateView.as_view(), name='update-guardian'),
    path('guardian/<int:pk>/delete/', GuardianDeleteView.as_view(), name='delete-guardian')
]