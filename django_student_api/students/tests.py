from django.test import TestCase

from .models import Student


class StudentModelTest(TestCase):

    def test_student_creation(self):

        student = Student.objects.create(
            name="Test Student",
            email="test@gmail.com",
            age=22,
            city="Pune"
        )

        self.assertEqual(
            student.name,
            "Test Student"
        )

        self.assertEqual(
            student.city,
            "Pune"
        )