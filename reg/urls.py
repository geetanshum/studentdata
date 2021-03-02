from django.urls import path
from .views import StudentView,StudentUpdateView,StudentDeleteView

urlpatterns = [
    path('',StudentView.as_view(),name="stuView"),
    path('student/edit/<int:pk>/',StudentUpdateView.as_view(),name="stuUpdate"),
    path('student/delete/<int:pk>/',StudentDeleteView.as_view(),name="stuDelete"),
]