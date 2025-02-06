from rest_framework import serializers

from apps.applications.models import ContactUsApplication


class ContactUsApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsApplication
        fields = (
            "id",
            "first_name",
            "last_name",
            "telegram_username",
            "phone_number",
            "inquiry_type",
            "consulting_agency",
            "message",
        )
