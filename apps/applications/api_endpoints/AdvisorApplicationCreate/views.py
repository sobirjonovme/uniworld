from rest_framework.generics import CreateAPIView

from apps.applications.models import AdvisorApplication

from .serializers import AdvisorApplicationCreateSerializer


class AdvisorApplicationCreateAPIView(CreateAPIView):
    queryset = AdvisorApplication.objects.all()
    serializer_class = AdvisorApplicationCreateSerializer


__all__ = ["AdvisorApplicationCreateAPIView"]
