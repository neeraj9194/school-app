from django.contrib import admin

from student.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'roll_number',
        'first_name',
        'last_name',
        'dob',
        'stream'
    )


admin.site.register(Student, StudentAdmin)

