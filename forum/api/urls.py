from django.urls import path
from forum.api import views

urlpatterns = [
    path('courses/<int:course_id>/discussions/', views.thread_list),
    path('courses/<int:course_id>/discussions/<int:pk>/', views.post_list),
]