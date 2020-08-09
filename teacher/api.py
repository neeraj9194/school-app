from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from teacher.models import StudentTeacherRelation


@api_view(['POST'])
def add_star(teacher_id, student_id):
    """
    API to add star from a student.
    """
    relation = get_object_or_404(
        StudentTeacherRelation.objects,
        {"student_id": student_id, "teacher_id": teacher_id}
    )
    relation.is_starred = True
    relation.date_starred = datetime.now()
    relation.save()
    return Response(status=HTTP_204_NO_CONTENT)


@api_view(['POST'])
def remove_star(teacher_id, student_id):
    """
    API to remove star from a student.
    """
    relation = get_object_or_404(
        StudentTeacherRelation.objects,
        {"student_id": student_id, "teacher_id": teacher_id}
    )
    relation.is_starred = False
    relation.date_starred = None
    relation.save()
    return Response(status=HTTP_204_NO_CONTENT)
