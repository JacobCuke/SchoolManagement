from django.urls import path
from . import views
from .views import (
    DiscussionThreadListView,
    DiscussionPostListView,
    DiscussionPostCreateView
)

urlpatterns = [
    path('course/<int:course_id>/discussions/', DiscussionThreadListView.as_view(), name='thread-list'),
    path('course/<int:course_id>/discussions/create/', views.create_thread, name='create-thread'),
    path('course/<int:course_id>/discussions/<int:pk>/', DiscussionPostListView.as_view(), name='post-list'),
    path('course/<int:course_id>/discussions/<int:pk>/create/', DiscussionPostCreateView.as_view(), name='create-post'),
]