# Generated by Django 5.0.4 on 2024-09-25 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="birthday",
            field=models.DateField(blank=True, null=True, verbose_name="生年月日"),
        ),
    ]
