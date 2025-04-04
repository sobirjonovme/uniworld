import os
from datetime import datetime

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.views import View
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser

from apps.common.services.dashboard import (
    get_applications_statistics_via_country,
    get_applications_statistics_via_gender,
    get_applications_statistics_via_region,
    get_applications_statistics_via_status, get_operators_statistics)


# Create your views here.
def index_page(self, request, extra_context=None):
    user = request.user
    extra_context = {
        "applications_status": get_applications_statistics_via_status(user),
        "applications_gender": get_applications_statistics_via_gender(user),
        "applications_region": get_applications_statistics_via_region(user),
        "applications_country": get_applications_statistics_via_country(user),
        "operators": get_operators_statistics(user),
    }

    template = "admin/index/main.html"
    app_list = self.get_app_list(request)
    context = {
        **self.each_context(request),
        "title": "Uniworld Dashboard",
        "subtitle": None,
        "app_list": app_list,
        **(extra_context or {}),
    }
    request.current_app = self.name
    return TemplateResponse(request, template, context)


class TinyMCEUploadView(View):
    permission_classes = (IsAdminUser,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        if request.FILES.get("file"):
            file = request.FILES["file"]
            file_name = default_storage.save(
                os.path.join("uploads", datetime.now().strftime("%Y/%m"), file.name), ContentFile(file.read())
            )
            file_url = default_storage.url(file_name)
            return JsonResponse({"location": file_url})
        return JsonResponse({"error": "Invalid request"}, status=400)
