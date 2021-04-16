from django.urls import path
from school.api import views

urlpatterns = [
    path('courses/', views.course_list),
    path('courses/<int:pk>/', views.course_detail),
    path('courses/<int:course_id>/lectures/', views.lecture_list),
    path('courses/<int:course_id>/assignments/', views.assignment_list),
    path('courses/<int:course_id>/enrollments/', views.enrollment_list),
    path('courses/<int:course_id>/enrollments/<int:student_id>/', views.enroll_detail),
    path('courses/<int:course_id>/assistants/', views.ta_list),
    path('courses/<int:course_id>/assistants/<int:student_id>/', views.ta_detail)
]
