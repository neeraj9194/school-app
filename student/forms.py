from django.forms import ModelForm, DateInput, NumberInput, Form, \
    ModelChoiceField

from student.models import Student
from teacher.models import Teacher


class CustomDateInput(DateInput):
    input_type = 'date'


class StudentForm(ModelForm):
    field_order = ['roll_number', 'first_name', 'last_name', 'dob', 'stream']
    success_url = '/'

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'dob': CustomDateInput(),
            'roll_number': NumberInput(),
        }

    def __init__(self, *args, **kwargs):
        """
        Add "placeholder" attribute as help text and set default class
        "form-control" in all input fields.
        """
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.help_text
            value.widget.attrs['class'] = "form-control"


class StudentStarForm(Form):
    """
    Form to star a student.
    """
    teacher = ModelChoiceField(label='Teacher', queryset=Teacher.objects.all())

    def __init__(self, *args, **kwargs):
        """
        Return only this teachers who teach given student aand have not
        already marked
        """
        student_id = kwargs.pop('student_id', None)
        if student_id:
            student = Student.objects.get(id=student_id)
            self.fields['teacher'].queryset = student.teacher.filter(
                studentteacherrelation__is_starred=False
            )
        super(StudentStarForm, self).__init__(*args, **kwargs)
