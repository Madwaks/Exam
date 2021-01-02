from django.contrib.auth.models import User
from django.db import models


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    @property
    def full_name(self):
        return self.user.username

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.username
