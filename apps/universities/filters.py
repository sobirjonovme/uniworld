from django_filters import rest_framework as filters
from drf_yasg import openapi

from .choices import QualificationLevels
from .models import University, UniversityCourse


class UniversityFilter(filters.FilterSet):
    full_scolarship = filters.BooleanFilter(method="filter_full_scolarship", label="Full scolarship")

    class Meta:
        model = University
        fields = ("country", "is_featured")

    def filter_full_scolarship(self, queryset, name, value):
        if value:
            return queryset.filter(full_scolarship=True)
        return queryset


class UniversityCourseFilter(filters.FilterSet):
    class Meta:
        model = UniversityCourse
        fields = ("specialty", "qualification_level")


UNIVERSITY_COURSE_FILTER_PARAMETERS = [
    openapi.Parameter("specialty", openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
    openapi.Parameter(
        "qualification_level",
        openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        enum=[level[0] for level in QualificationLevels.choices],
    ),
]
