from django.urls import path

from teacher.views import TeacherView

urlpatterns = [
    path('', TeacherView.as_view(template_name="teacher.html")),
]
