import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onlinequiz.settings")
import django
import pytest
from django.conf import settings


def pytest_configure():
    settings.DEBUG = False
    settings.LANGUAGE_CODE = "en"
    settings.USE_I18N = False
    django.setup()
