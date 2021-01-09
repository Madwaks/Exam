import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onlinequiz.settings")


def pytest_configure():
    settings.DEBUG = False
    settings.LANGUAGE_CODE = "en"
    settings.USE_I18N = False
    django.setup()
