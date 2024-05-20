# Generated by Django 5.0.6 on 2024-05-18 18:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("consultations", "0007_remove_theme_unique_up_to_question_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="consultation",
            constraint=models.UniqueConstraint(fields=("slug",), name="unique_consultation_slug"),
        ),
    ]