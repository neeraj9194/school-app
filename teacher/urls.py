from django.urls import path

from teacher.views import TeacherView

urlpatterns = [
    path('', TeacherView.as_view(), name="list"),
    path('<int:pk>/', TeacherView.as_view(), name="detail")
]
