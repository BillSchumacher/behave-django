from django.db import models
from django.contrib.auth.models import AbstractUser


class BehaveTestModel(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()

    def get_absolute_url(self):
        return '/behave/test/%i/%s' % (self.number, self.name)


class CustomUser(AbstractUser):
    pass
