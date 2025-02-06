from rest_framework import serializers

from apps.organizations.models import Agency


class AgencyShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = (
            "id",
            "name"
        )
