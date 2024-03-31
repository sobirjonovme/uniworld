from rest_framework.generics import CreateAPIView

from apps.applications.models import Application

from .serializers import ApplicationCreateSerializer


class ApplicationCreateAPIView(CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationCreateSerializer


__all__ = ["ApplicationCreateAPIView"]
