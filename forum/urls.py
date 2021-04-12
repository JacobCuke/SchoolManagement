from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/forum/create/', views.create_thread, name='create-thread'),
]