from django.db import models


class Teacher(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    subject = models.CharField(max_length=100)

    experience = models.PositiveIntegerField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name