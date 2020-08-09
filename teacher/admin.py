from django.contrib import admin

from teacher.models import Teacher, StudentTeacherRelation


class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'subject'
    )


class StudentTeacherRelationAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'teacher',
        'is_starred',
        'date_starred'
    )


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(StudentTeacherRelation, StudentTeacherRelationAdmin)

