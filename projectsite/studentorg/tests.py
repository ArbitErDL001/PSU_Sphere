from django.test import TestCase
from django.urls import reverse

from .models import College, Program, Student


class StudentEditTests(TestCase):
    def setUp(self):
        self.college = College.objects.create(college_name="Test College")
        self.program = Program.objects.create(prog_name="Computer Science", college=self.college)
        self.student = Student.objects.create(
            student_id="CS001",
            lastname="Doe",
            firstname="Jane",
            program=self.program,
        )

    def test_student_edit_route_updates_record(self):
        response = self.client.post(
            reverse("student-edit", args=[self.student.pk]),
            {
                "student_id": "CS002",
                "lastname": "Smith",
                "firstname": "John",
                "middlename": "",
                "program": self.program.pk,
            },
        )

        self.student.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("student-list"))
        self.assertEqual(self.student.student_id, "CS002")
        self.assertEqual(self.student.lastname, "Smith")
        self.assertEqual(self.student.firstname, "John")
