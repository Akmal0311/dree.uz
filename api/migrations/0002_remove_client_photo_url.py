# Generated by Django 4.1 on 2022-08-23 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='photo_url',
        ),
    ]