from django.urls import path
from school.api import views

urlpatterns = [
    path('courses/', views.course_list),
    path('courses/<int:pk>/', views.course_detail),
    path('courses/<int:course_id>/lectures/', views.lecture_list),
    path('courses/<int:course_id>/assignments/', views.assignment_list),
    path('courses/<int:course_id>/enrollments/', views.enrollment_list)
]
