from datetime import date

# Create your tests here.
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from student.models import Student
from teacher.models import Teacher, StudentTeacherRelation


class TestRewardAPI(APITestCase):
    def setUp(self):
        self.student1 = Student.objects.create(
            first_name="John",
            last_name="Oliver",
            dob=date.today(),
            stream="CS",
            roll_number="111"
        )
        self.teacher1 = Teacher.objects.create(
            first_name="John",
            last_name="Mcclane",
            subject="CS",
        )
        # Auth
        user1 = User.objects.create(username='test_1', first_name='test_1',
                                    last_name='test1')
        self.client.force_authenticate(user=user1)

    def test_404_add_star(self):
        """
        Adding star will give 404 if relation does not exist.
        """
        response = self.client.post(
            '/teacher/{t_id}/reward/student/{s_id}/remove/'.format(
                t_id=self.teacher1.id, s_id=self.student1.id), format='json'
        )
        self.assertEquals(404, response.status_code)

    def test_add_star(self):
        """
        Test star is added correctly to Teacher-Student relationship.
        """
        # Adding relation
        relation = StudentTeacherRelation.objects.create(
            teacher=self.teacher1,
            student=self.student1,
        )
        response = self.client.post(
            '/teacher/{t_id}/reward/student/{s_id}/add/'.format(
                t_id=self.teacher1.id, s_id=self.student1.id), format='json'
        )
        self.assertEquals(204, response.status_code)
        relation_changed = StudentTeacherRelation.objects.get(id=relation.id)
        self.assertEqual(True, relation_changed.is_starred)

    def test_remove_star(self):
        """
        Test star is removed correctly to Teacher-Student relationship.
        """
        # Adding relation
        relation = StudentTeacherRelation.objects.create(
            teacher=self.teacher1,
            student=self.student1,
        )
        response = self.client.post(
            '/teacher/{t_id}/reward/student/{s_id}/remove/'.format(
                t_id=self.teacher1.id, s_id=self.student1.id), format='json'
        )
        self.assertEquals(204, response.status_code)
        relation_changed = StudentTeacherRelation.objects.get(id=relation.id)
        self.assertEqual(False, relation_changed.is_starred)
