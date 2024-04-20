from rest_framework.pagination import LimitOffsetPagination


class CoursePagination(LimitOffsetPagination):
    default_limit = 200
