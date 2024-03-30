from rest_framework import serializers

from apps.universities.models import Specialty


class SpecialtyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ("id", "name")
