from django.db import models
from teachers.models import Teacher


class Course(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField()

    duration_months = models.PositiveIntegerField()

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name