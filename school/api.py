from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, \
    permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from student.models import Student
from teacher.models import Teacher, StudentTeacherRelation


@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
    """
    Returns dashboard stats, like
     - Number of students
     - Number of teachers
     - NUmber of stars received.
    """
    num_students = Student.objects.count()
    num_teachers = Teacher.objects.count()
    num_stars = StudentTeacherRelation.objects.filter(is_starred=True).count()
    data = {
        "students": num_students,
        "teachers": num_teachers,
        "stars": num_stars,
    }
    return Response(data=data, status=HTTP_200_OK)
