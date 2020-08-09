from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView

from teacher.forms import TeacherForm
from teacher.models import Teacher


class TeacherView(LoginRequiredMixin, CreateView):
    """
    A Teacher view responsible to Create/List Teacher model.
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


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    """
    A Teacher view responsible to Update object in Teacher model.
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


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    """
    A Teacher view responsible to Delete in Teacher model.
    """
    form_class = TeacherForm
    model = Teacher
    success_url = '/teacher/'
    template_name = "teacher.html"


@login_required
def reward_list(request):
    """
    List all teachers with their students with star status.
    """
    teachers = Teacher.objects.all().prefetch_related(
        'studentteacherrelation_set__student'
    ).distinct()
    return render(request, 'rewards.html', {'teachers': teachers})
