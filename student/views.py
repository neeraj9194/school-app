from django.views.generic import CreateView, UpdateView

from student.forms import StudentForm
from student.models import Student


class StudentView(CreateView, UpdateView):
    form_class = StudentForm
    model = Student
    success_url = '/student/'
    template_name = "student/student.html"

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Student.objects.all()
        return super(StudentView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        """
        Update "get" to accept both URLs.
        """
        if kwargs.get('pk'):
            self.object = self.get_object()
        else:
            self.object = None
        return self.render_to_response(self.get_context_data())

