from datetime import date

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from student.models import Student
from teacher.models import Teacher, StudentTeacherRelation


class TestDashboardAPI(APITestCase):
    def setUp(self):
        student1 = Student.objects.create(
            first_name="John",
            last_name="Oliver",
            dob=date.today(),
            stream="CS",
            roll_number="111"
        )
        teacher1 = Teacher.objects.create(
            first_name="John",
            last_name="Mcclane",
            subject="CS",
        )
        relation = StudentTeacherRelation.objects.create(
            teacher=teacher1,
            student=student1,
            is_starred=True
        )

        # Auth
        user1 = User.objects.create(username='test_1', first_name='test_1',
                                    last_name='test1')
        self.client.force_authenticate(user=user1)

    def test_stats_api(self):
        """
        Tests should return correct stats.
        """
        response = self.client.get('/dashboard/stats/', format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual({
            "students": 1,
            "teachers": 1,
            "stars": 1
        }, response.data)
