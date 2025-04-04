from django.db.models import Count, OuterRef, Subquery
from rest_framework import serializers

from apps.common.serializers import CountrySerializer
from apps.universities.models import RequiredDocument, Specialty, University


class RequiredDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredDocument
        fields = ("id", "document_type", "description")
        ref_name = "UniversityRequiredDocumentSerializer"


class UniversitySpecialtyListSerializer(serializers.ModelSerializer):
    course_count = serializers.IntegerField()

    class Meta:
        model = Specialty
        fields = ("id", "name", "course_count")


class UniversityDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    required_documents = RequiredDocumentSerializer(many=True, read_only=True)
    specialties = serializers.SerializerMethodField()

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
            "free_consultation",
            "country",
            "institution_type",
            "establishment_year",
            "has_dormitory",
            "students_count",
            "address",
            "about",
            "scholarship_description",
            "intake_months",
            "tuition_fee",
            "application_fee",
            "living_cost",
            "visa_fee",
            "required_documents",
            "specialties",
        )

    def get_specialties(self, obj):
        courses = obj.courses.all()

        specialties_qs = Specialty.objects.filter(courses__university_id=obj.id).distinct()
        specialties_qs = specialties_qs.annotate(
            course_count=Subquery(
                courses.filter(specialty=OuterRef("id"))
                .values("specialty")
                .annotate(course_count=Count("id"))
                .values("course_count")
            )
        )

        return {
            "total_courses": courses.count(),
            "data": UniversitySpecialtyListSerializer(specialties_qs, many=True).data,
        }
