from django.urls import path

from student.views import StudentList

urlpatterns = [
    path('', StudentList.as_view(template_name="student/student.html")),
]
