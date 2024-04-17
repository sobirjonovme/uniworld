from .base import *  # noqa

###################################################################
# General
###################################################################

DEBUG = False

###################################################################
# Django security
###################################################################

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://uniworld.xn--0h8h.uz",
    "https://uniworld.xn--0h8h.uz",
    "http://panel.uniworld.uz",
    "https://panel.uniworld.uz",
]

###################################################################
# CORS
###################################################################

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]
