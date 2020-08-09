from django.urls import path

from teacher.api import RewardAPI
from teacher.views import TeacherView, TeacherUpdateView, TeacherDeleteView, \
    reward_list

urlpatterns = [
    path('', TeacherView.as_view(), name="list"),
    path('<int:pk>/', TeacherUpdateView.as_view(), name="detail"),
    path('<int:pk>/delete/', TeacherDeleteView.as_view(), name="delete"),
    path('rewards/', reward_list, name="reward-list"),

    # REST APIs
    path('<int:teacher_id>/reward/student/<int:student_id>/add', RewardAPI.as_view()),
    path('<int:teacher_id>/reward/student/<int:student_id>/remove', RewardAPI.as_view()),
]
