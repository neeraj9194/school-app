from django.urls import path

from teacher.views import TeacherView, TeacherUpdateView, TeacherDeleteView

urlpatterns = [
    path('', TeacherView.as_view(), name="list"),
    path('<int:pk>/', TeacherUpdateView.as_view(), name="detail"),
    path('<int:pk>/delete/', TeacherDeleteView.as_view(), name="delete")
]
