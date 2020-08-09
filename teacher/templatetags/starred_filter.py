from django import template


register = template.Library()


@register.filter(name="filter_starred")
def teachers_marked_star(teacher):
    """
    Return only teachers that a student who marked them with star.
    """
    return teacher.filter(studentteacherrelation__is_starred=True)
