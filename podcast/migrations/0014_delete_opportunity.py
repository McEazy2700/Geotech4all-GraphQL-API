# Generated by Django 3.2.9 on 2023-04-06 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0013_podcast_cover_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Opportunity',
        ),
    ]