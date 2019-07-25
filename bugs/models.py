from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Bug(models.Model):
    name = models.CharField(max_length=75)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.name