from apps.applications.models import AdvisorApplication
from apps.universities.models import University, UniversityCourse


def get_matched_universities(application: AdvisorApplication):
    try:
        user_certificates = {item["certificate"]: item["score"] for item in application.certificates}
    except Exception:
        user_certificates = {}

    courses_qs = UniversityCourse.objects.filter(
        specialty_id=application.needed_specialty_id,
        qualification_level=application.needed_education_level,
    )
    university_scores = {}  # type: ignore

    for course in courses_qs:
        old_score = university_scores.get(course.university_id, 0)
        new_score = 0
        for ar in course.admission_requirements.all():
            if ar.requirement in user_certificates:
                new_score += 1
        university_scores[course.university_id] = max(old_score, new_score)

    sorted_universities = sorted(university_scores.items(), key=lambda x: x[1], reverse=True)
    high_priority_universities_ids = [university_id for university_id, _ in sorted_universities[:4]]

    return University.objects.filter(id__in=high_priority_universities_ids).select_related("country")
