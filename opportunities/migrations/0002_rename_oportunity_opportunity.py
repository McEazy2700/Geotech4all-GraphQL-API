# Generated by Django 3.2.9 on 2023-04-06 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
        ('opportunities', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Oportunity',
            new_name='Opportunity',
        ),
    ]