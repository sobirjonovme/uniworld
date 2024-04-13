from rest_framework import serializers

from apps.common.models import PrivacyPolicy


class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = ("policy",)
