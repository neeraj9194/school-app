from django.views.generic import CreateView, UpdateView

from teacher.forms import TeacherForm
from teacher.models import Teacher


class TeacherView(CreateView, UpdateView):
    """
    A Teacher view responsible for
     - Create/Update/Delete in Teacher model.
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

    def get(self, request, *args, **kwargs):
        """
        Update "get" to accept both URLs i.e with `pk` and without.
        """
        if kwargs.get('pk'):
            self.object = self.get_object()
        else:
            self.object = None
        return self.render_to_response(self.get_context_data())
