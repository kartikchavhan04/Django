from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "email",
        "subject",
        "experience",
        "is_active",
    )

    search_fields = (
        "name",
        "email",
        "subject",
    )

    list_filter = (
        "subject",
        "is_active",
    )