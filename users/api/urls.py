from django.urls import path
from users.api import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', obtain_auth_token),
    path('users/', views.create_user),
    path('users/<int:pk>/', views.delete_user),
    path('users/students/', views.student_list),
    path('users/students/<int:pk>/', views.student_detail),
    path('users/students/<int:pk>/enrollments/', views.student_enrollments),
    path('users/students/<int:pk>/assistances/', views.student_assitances),
    path('users/students/<int:pk>/guardians/', views.student_guardians),
    path('users/students/<int:pk>/extracurriculars/', views.student_extracurriculars),
    path('users/instructors/', views.instructor_list),
    path('users/instructors/<int:pk>/', views.instructor_detail),
    path('users/instructors/<int:pk>/courses/', views.instructor_courses),
]