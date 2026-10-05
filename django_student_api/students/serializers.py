from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student

        fields = [
            "id",
            "name",
            "email",
            "age",
            "city",
            "is_active",
            "created_at",
        ]

    def validate(self, attrs):

        allowed_fields = {
            "name",
            "email",
            "age",
            "city",
            "is_active",
        }

        extra_fields = set(self.initial_data.keys()) - allowed_fields

        if extra_fields:
            raise serializers.ValidationError({
                "error": f"Unknown fields: {list(extra_fields)}"
            })

        return attrs