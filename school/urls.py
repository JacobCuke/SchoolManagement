from django.urls import path
from . import views
from .views import (
    DashboardListView,
    CourseDetailView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<str:username>/', DashboardListView.as_view(), name='user-dashboard'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course-detail')
]