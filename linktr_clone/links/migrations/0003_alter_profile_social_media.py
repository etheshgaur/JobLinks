# Generated by Django 4.2.3 on 2024-08-16 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='social_media',
            field=models.URLField(blank=True, null=True),
        ),
    ]