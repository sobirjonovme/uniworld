from django.contrib.auth.models import UserManager

from .choices import UserRoles


class OperatorManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role=UserRoles.AGENCY_OPERATOR)
