from django.views.generic import CreateView, UpdateView

from teacher.forms import TeacherForm
from teacher.models import Teacher


class TeacherView(CreateView, UpdateView):
    form_class = TeacherForm
    model = Teacher
    # fields = '__all__'
    success_url = '/teacher/'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Teacher.objects.all().prefetch_related('student')
        return super(TeacherView, self).get_context_data(**kwargs)

