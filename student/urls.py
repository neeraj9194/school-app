from django.urls import path

from student.views import StudentView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('', StudentView.as_view(), name="list"),
    path('<int:pk>/', StudentUpdateView.as_view(), name="detail"),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name="delete")
]
