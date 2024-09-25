from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20
    )

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    user = models.ForeignKey(
        to=CustomUser,
        verbose_name='ユーザ',
        on_delete=models.CASCADE,
        null=True
    )

    category = models.ForeignKey(
        to=Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT,
        null=True
    )

    title = models.CharField(
        verbose_name='タイトル',
        max_length=20
    )

    content = models.TextField(
        verbose_name='本文'
    )

    posted_id = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )

    image = models.ImageField(				
        verbose_name='イメージ',				
        upload_to ='photos',				
        null = True,						
        blank=True,							
    )

    def __str__(self):
        return self.title
