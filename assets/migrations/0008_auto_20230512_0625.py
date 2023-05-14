# Generated by Django 3.2.9 on 2023-05-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_alter_image_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('public_id', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('folder', models.CharField(choices=[('PODCAST', 'Podcast')], max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='folder',
            field=models.CharField(choices=[('BLOG', 'Blog'), ('PODCAST', 'Podcast'), ('PROFILE', 'Profile'), ('OPPORTUNITY', 'Opportunity')], max_length=50, null=True),
        ),
    ]
