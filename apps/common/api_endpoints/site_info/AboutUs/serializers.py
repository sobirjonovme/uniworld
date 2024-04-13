from rest_framework import serializers

from apps.common.models import AboutUs


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ("find_university", "our_services", "card_title", "card_body")
