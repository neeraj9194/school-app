from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView

from student.forms import StudentForm
from student.models import Student


class StudentView(LoginRequiredMixin, CreateView):
    """
    A Student view responsible for
     - Create/List in Student model.
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


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    """
    A Student view responsible to Update in Student model.
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
        return super(StudentUpdateView, self).get_context_data(**kwargs)


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    """
    A Student view responsible for Delete an object in Student model.
    """
    form_class = StudentForm
    model = Student
    success_url = '/student/'
    template_name = "student/student.html"
