# Generated by Django 4.2.6 on 2023-11-01 12:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Monarch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "campaign_name",
                    models.SlugField(unique=True, verbose_name="Campaign name"),
                ),
                (
                    "current_stress",
                    models.IntegerField(verbose_name="Monarch Current Stress Level"),
                ),
            ],
        ),
    ]
