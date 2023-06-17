# Generated by Django 3.2.9 on 2023-06-16 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0008_auto_20230512_0625'),
        ('common', '0001_initial'),
        ('opportunities', '0008_auto_20230616_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='location',
            field=models.ManyToManyField(blank=True, to='common.Location'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.organization'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='tags',
            field=models.ManyToManyField(related_name='opportunities', to='assets.Tag'),
        ),
    ]
