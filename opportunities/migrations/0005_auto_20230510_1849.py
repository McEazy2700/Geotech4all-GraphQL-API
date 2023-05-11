# Generated by Django 3.2.9 on 2023-05-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0004_alter_opportunity_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opportunity',
            old_name='description',
            new_name='abstract',
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='images',
        ),
        migrations.AddField(
            model_name='opportunity',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
