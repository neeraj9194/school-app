from django.urls import path

from teacher.views import TeacherView, TeacherUpdateView, TeacherDeleteView, \
    reward_list

urlpatterns = [
    path('', TeacherView.as_view(), name="list"),
    path('<int:pk>/', TeacherUpdateView.as_view(), name="detail"),
    path('<int:pk>/delete/', TeacherDeleteView.as_view(), name="delete"),
    path('rewards/', reward_list, name="reward-list")
]
