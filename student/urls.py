from django.urls import path

from student.views import StudentView, StudentUpdateView

urlpatterns = [
    path('', StudentView.as_view(), name="list"),
    path('<int:pk>/', StudentUpdateView.as_view(), name="detail"),
    path('<int:pk>/delete/', StudentUpdateView.as_view(), name="delete")
]
