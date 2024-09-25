from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birthday = models.DateField(
        verbose_name='生年月日',
        null=True,
        blank=True
    )
