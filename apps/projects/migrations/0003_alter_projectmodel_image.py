# Generated by Django 4.2.4 on 2023-08-29 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_projectmodel_progress_alter_projectmodel_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectmodel",
            name="image",
            field=models.ImageField(
                blank=True,
                default="projects/banner.jpg",
                null=True,
                upload_to="projects/",
            ),
        ),
    ]
