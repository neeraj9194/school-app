from django.views.generic import CreateView, UpdateView, DeleteView

from teacher.forms import TeacherForm
from teacher.models import Teacher


class TeacherView(CreateView):
    """
    A Teacher view responsible for
     - Create/List in Teacher model.
    """
    form_class = TeacherForm
    model = Teacher
    success_url = '/teacher/'
    template_name = "teacher.html"

    def get_context_data(self, **kwargs):
        """
        Update CreateView context with "list" of Teachers(students prefetched).
        """
        kwargs['object_list'] = Teacher.objects.all().prefetch_related('student')
        return super(TeacherView, self).get_context_data(**kwargs)


class TeacherUpdateView(UpdateView, DeleteView):
    """
    A Teacher view responsible for
     - Update/Delete in Teacher model.
    """
    form_class = TeacherForm
    model = Teacher
    success_url = '/teacher/'
    template_name = "teacher.html"

    def get_context_data(self, **kwargs):
        """
        Update CreateView context with "list" of Teachers(students prefetched).
        """
        kwargs['object_list'] = Teacher.objects.all().prefetch_related('student')
        return super(TeacherUpdateView, self).get_context_data(**kwargs)
