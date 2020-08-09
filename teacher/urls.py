from django.urls import path

from teacher.api import add_star, remove_star
from teacher.views import TeacherView, TeacherUpdateView, TeacherDeleteView, \
    reward_list

urlpatterns = [
    path('', TeacherView.as_view(), name="list"),
    path('<int:pk>/', TeacherUpdateView.as_view(), name="detail"),
    path('<int:pk>/delete/', TeacherDeleteView.as_view(), name="delete"),
    path('rewards/', reward_list, name="reward-list"),

    # REST APIs
    path('<int:teacher_id>/reward/student/<int:student_id>/add/', add_star),
    path('<int:teacher_id>/reward/student/<int:student_id>/remove/', remove_star)
]
