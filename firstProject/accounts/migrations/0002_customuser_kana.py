# Generated by Django 5.0.4 on 2024-09-25 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="kana",
            field=models.CharField(
                blank=True, max_length=40, null=True, verbose_name="氏名カナ"
            ),
        ),
    ]
