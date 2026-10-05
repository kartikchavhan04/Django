from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "email",
        "age",
        "city",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "city",
    )

    list_filter = (
        "city",
        "is_active",
    )

    ordering = (
        "-created_at",
    )