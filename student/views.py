from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView

from student.forms import StudentForm, StudentStarForm
from student.models import Student
from teacher.models import StudentTeacherRelation


class StudentView(CreateView):
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
        kwargs['star_form'] = StudentStarForm()
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


class StudentUpdateView(UpdateView):
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


class StudentDeleteView(DeleteView):
    """
    A Student view responsible for Delete an object in Student model.
    """
    form_class = StudentForm
    model = Student
    success_url = '/student/'
    template_name = "student/student.html"


def add_star(request, pk):
    """
    Star a student.
    """
    if request.method == 'POST':
        form = StudentStarForm(request.POST)
        if form.is_valid():
            relationship = StudentTeacherRelation.objects.get(
                student_id=pk,
                teacher=form.cleaned_data['teacher'],
            )
            relationship.is_starred = True
            relationship.date_starred = datetime.now()
            relationship.save()
            return HttpResponseRedirect('/student/')
    else:
        form = StudentStarForm()

    return render(request, 'student/student.html', {'star_form': form})
