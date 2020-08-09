from django.contrib import admin

from teacher.models import Teacher, StudentTeacherRelation


class TeacherAdmin(admin.ModelAdmin):
    pass


class StudentTeacherRelationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(StudentTeacherRelation, StudentTeacherRelationAdmin)

