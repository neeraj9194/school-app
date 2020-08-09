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
        related_name="teacher",
        through='StudentTeacherRelation'
    )
    # image =

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


class StudentTeacherRelation(models.Model):
    """
    A relationship model between Student and Teacher with a star boolean that
    can be marked by a teacher for a student.
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    is_starred = models.BooleanField(
        default=False,
        help_text="Whether student is starred by the teacher."
    )
    date_starred = models.DateTimeField(
        help_text="Date time the student is starred.",
        null=True, blank=True
    )
