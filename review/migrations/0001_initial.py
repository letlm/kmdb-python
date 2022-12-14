# Generated by Django 4.1 on 2022-08-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("stars", models.IntegerField()),
                ("review", models.TextField()),
                ("spoilers", models.BooleanField(blank=True, default=False, null=True)),
                (
                    "recomendation",
                    models.CharField(
                        choices=[
                            ("Must Watch", "Must Watch"),
                            ("Should Watch", "Should Watch"),
                            ("Avoid Watch", "Avoid Watch"),
                            ("No Opinion", "No Opinion"),
                        ],
                        default="No Opinion",
                        max_length=50,
                    ),
                ),
            ],
        ),
    ]
