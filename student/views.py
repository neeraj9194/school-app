from django.views.generic import CreateView

from student.forms import StudentForm
from student.models import Student


class StudentView(CreateView):
    form_class = StudentForm
    model = Student
    success_url = '/student/'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Student.objects.all()
        return super(StudentView, self).get_context_data(**kwargs)

