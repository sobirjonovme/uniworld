from rest_framework import serializers

from apps.common.serializers import CountrySerializer
from apps.universities.models import RequiredDocument, University


class RequiredDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredDocument
        fields = ("id", "document_type", "description")
        ref_name = "UniversityRequiredDocumentSerializer"


class UniversityDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    required_documents = RequiredDocumentSerializer(many=True, read_only=True)

    class Meta:
        model = University
        fields = (
            "id",
            "name",
            "image",
            "logo",
            "slug",
            "is_featured",
            "full_scolarship",
            "country",
            "institution_type",
            "address",
            "about",
            "intake_months",
            "tuition_fee",
            "application_fee",
            "living_cost",
            "visa_fee",
            "required_documents",
        )
