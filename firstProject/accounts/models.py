from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    kana = models.CharField(				
        verbose_name='氏名カナ',				
        max_length=40,			
        null = True,						
        blank=True,							
    )
