from django.views.generic import ListView

from student.models import Student


class StudentList(ListView):
    model = Student
