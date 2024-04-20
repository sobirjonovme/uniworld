from rest_framework.pagination import LimitOffsetPagination


class CountryPagination(LimitOffsetPagination):
    default_limit = 50
