from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "teacher",
        "duration_months",
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    list_filter = (
        "teacher",
        "is_active",
    )