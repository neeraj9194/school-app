from django.views.generic import CreateView, UpdateView

from student.forms import StudentForm
from student.models import Student


class StudentView(CreateView, UpdateView):
    """
    A Student view responsible for
     - Create/Update/Delete in Student model.
    """
    form_class = StudentForm
    model = Student
    success_url = '/student/'
    template_name = "student/student.html"

    def get_context_data(self, **kwargs):
        """
        Update CreateView context with "list" of Students.
        """
        kwargs['object_list'] = Student.objects.all()
        return super(StudentView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        """
        Update "get" to accept both URLs i.e with `pk` and without.
        """
        if kwargs.get('pk'):
            self.object = self.get_object()
        else:
            self.object = None
        return self.render_to_response(self.get_context_data())

