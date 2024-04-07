from rest_framework import serializers

from apps.applications.models import Application
from apps.tgbot.services.applications import send_application_info_to_operator
from apps.users.models import User, UserRoles


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
        operator = User.objects.filter(
            agency=application.agency, role=UserRoles.AGENCY_OPERATOR, countries__country=application.university.country
        ).first()
        application.operator = operator
        application.save()

        if operator:
            send_application_info_to_operator(application)

        return application
