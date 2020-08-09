from datetime import datetime

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, \
    permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from teacher.models import StudentTeacherRelation


@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def add_star(request, teacher_id, student_id):
    """
    API to add star from a student.
    """
    try:
        relation = StudentTeacherRelation.objects.get(
            student_id=student_id, teacher_id=teacher_id
        )
    except StudentTeacherRelation.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    relation.is_starred = True
    relation.date_starred = datetime.now()
    relation.save()
    return Response(status=HTTP_204_NO_CONTENT)


@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def remove_star(request, teacher_id, student_id):
    """
    API to remove star from a student.
    """
    try:
        relation = StudentTeacherRelation.objects.get(
            student_id=student_id, teacher_id=teacher_id
        )
    except StudentTeacherRelation.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    relation.is_starred = False
    relation.date_starred = None
    relation.save()
    return Response(status=HTTP_204_NO_CONTENT)
