# Generated by Django 4.1.6 on 2023-02-28 18:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("review", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="body",
            field=models.TextField(max_length=8192),
        ),
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.PositiveSmallIntegerField(
                max_length=1024,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="description",
            field=models.TextField(blank=True, max_length=2048),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
