from django.forms import ModelForm, SelectMultiple

from teacher.models import Teacher


class TeacherForm(ModelForm):
    field_order = ['first_name', 'last_name', 'subject', 'student']
    success_url = '/'

    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'student': SelectMultiple(attrs={'size': '8'}),
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
