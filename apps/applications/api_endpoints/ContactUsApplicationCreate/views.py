from rest_framework.generics import CreateAPIView

from apps.applications.models import ContactUsApplication

from .serializers import ContactUsApplicationCreateSerializer


class ContactUsApplicationCreateAPIView(CreateAPIView):
    queryset = ContactUsApplication.objects.all()
    serializer_class = ContactUsApplicationCreateSerializer


__all__ = ["ContactUsApplicationCreateAPIView"]
