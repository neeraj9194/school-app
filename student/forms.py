from django.forms import ModelForm, DateInput, NumberInput

from student.models import Student


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
