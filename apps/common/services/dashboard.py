from django.db import models

from apps.applications.choices import ApplicationStatus
from apps.applications.models import Application
from apps.common.choices import GenderChoices
from apps.common.models import Country, Region
from apps.users.choices import UserRoles


def get_color(index):
    colors_list = [
        "#1BC5BD",
        "#EB9F40",
        "#61A4F6",
        "#61C571",
        "#DD5D88",
        "#4FB2FF",
        "#6D2F85",
        "#1B87C5",
        "#F64D60",
        "#F6BD16",
    ]
    num = len(colors_list)
    return colors_list[index % num]


def get_applications(user):
    if user.is_superuser:
        applications = Application.objects.all()
    elif user.role == UserRoles.AGENCY_OWNER:
        applications = Application.objects.filter(agency=user.agency)
    else:
        applications = None

    return applications


def get_applications_statistics_via_status(user):
    applications = get_applications(user)
    if applications is None:
        return

    total_applications = applications.count()
    applications_stats = applications.values("status").annotate(count=models.Count("status"))

    data = {}
    for status in ApplicationStatus.values:
        status_count = (
            applications_stats.get(status=status)["count"] if applications_stats.filter(status=status).exists() else 0
        )
        data[status] = {
            "count": status_count,
            "percentage": round(status_count / total_applications * 100, 2) if total_applications else 0,
        }

    return data


def get_applications_statistics_via_gender(user):
    applications = get_applications(user)
    if applications is None:
        return

    total_applications = applications.count()
    applications_stats = applications.values("gender").annotate(count=models.Count("gender"))

    male_count = (
        applications_stats.get(gender=GenderChoices.MALE)["count"]
        if applications_stats.filter(gender=GenderChoices.MALE).exists()
        else 0
    )
    male_percentage = round(male_count / total_applications * 100, 2) if total_applications else 0
    female_count = (
        applications_stats.get(gender=GenderChoices.FEMALE)["count"]
        if applications_stats.filter(gender=GenderChoices.FEMALE).exists()
        else 0
    )
    female_percentage = round(female_count / total_applications * 100, 2) if total_applications else 0

    data = {
        "counts": [male_count, female_count],
        "percentages": [male_percentage, female_percentage],
        "gender_names": [GenderChoices.MALE.label, GenderChoices.FEMALE.label],
    }

    return data


def get_applications_statistics_via_region(user):
    applications = get_applications(user)
    if applications is None:
        return

    total_applications = applications.count()
    applications_stats = applications.values("region").annotate(count=models.Count("region"))

    counts = []
    percentages = []
    region_names = []

    for region in applications_stats:
        counts.append(region["count"])
        percentages.append(round(region["count"] / total_applications * 100, 2) if total_applications else 0)
        region_names.append(Region.objects.get(pk=region["region"]).name)

    data = {"counts": counts, "percentages": percentages, "region_names": region_names}

    return data


def get_applications_statistics_via_country(user):
    applications = get_applications(user)
    if applications is None:
        return

    total_applications = applications.count()
    applications_stats = applications.values("university__country").annotate(count=models.Count("university__country"))
    countries_count = applications_stats.count()

    all_datas = []
    divided_datas = []

    for country in applications_stats:
        all_datas.append(
            {
                "country": Country.objects.get(pk=country["university__country"]).name,
                "count": country["count"],
                "percentage": round(country["count"] / total_applications * 100, 2) if total_applications else 0,
            }
        )

    # sort countries by count
    all_datas = sorted(all_datas, key=lambda x: x["count"], reverse=True)
    # add colors to countries
    for index, temp_data in enumerate(all_datas):
        temp_data["color"] = get_color(index)

    for i in range(0, countries_count, 2):
        divided_datas.append({"left": all_datas[i], "right": all_datas[i + 1] if i + 1 < countries_count else None})

    data = {"total_applications": total_applications, "all_datas": all_datas, "divided_datas": divided_datas}

    return data
