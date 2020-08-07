from django.db import models

from student.models import Student


class Teacher(models.Model):
    """
    A teacher model.
    """
    first_name = models.CharField(
        max_length=100,
        help_text="First name of the teacher."
    )
    last_name = models.CharField(
        max_length=100,
        help_text="First name of the teacher."
    )
    subject = models.CharField(
        max_length=150,
        help_text="Subject which teacher teaches."
    )
    student = models.ManyToManyField(
        Student,
        help_text="Students taught by the teacher",
        related_name="teacher"
    )
    # image =

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

