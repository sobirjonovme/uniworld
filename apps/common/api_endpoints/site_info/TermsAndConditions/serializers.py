from rest_framework import serializers

from apps.common.models import TermsAndConditions


class TermsAndConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsAndConditions
        fields = ("terms",)
