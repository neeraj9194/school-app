from django.db import models


class Student(models.Model):
    """
    A student model.
    """
    first_name = models.CharField(
        max_length=100,
        help_text="First name of the student."
    )
    last_name = models.CharField(
        max_length=100,
        help_text="Last name of the student."
    )
    dob = models.DateField(
        help_text="Date of birth."
    )
    stream = models.CharField(
        max_length=100,
        help_text="Field of study."
    )
    roll_number = models.CharField(
        max_length=10,
        help_text="Roll number of student",
        unique=True
    )
    # image =

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
