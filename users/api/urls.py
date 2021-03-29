from django.urls import path
from users.api import views

urlpatterns = [
    path('users/students/', views.student_list),
    path('users/students/<int:pk>/', views.student_detail),
    path('users/students/<int:pk>/enrollments/', views.student_enrollments),
    path('users/students/<int:pk>/assistances/', views.student_assitances),
    path('users/instructors/', views.instructor_list),
    path('users/instructors/<int:pk>/', views.instructor_detail),
]