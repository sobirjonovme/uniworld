from rest_framework import serializers

from apps.applications.models import Application


class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = (
            "id",
            "university",
            "course",
            "first_name",
            "last_name",
            "age",
            "phone_number",
            "email",
            "gender",
            "region",
        )
        extra_kwargs = {
            "university": {"required": True, "allow_null": False},
        }

    def create(self, validated_data):
        application = Application(**validated_data)
        application.agency = application.university.agency
        application.save()

        return application
