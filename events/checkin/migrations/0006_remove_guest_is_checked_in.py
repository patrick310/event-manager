# Generated by Django 2.0.3 on 2018-09-04 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0005_auto_20180903_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='is_checked_in',
        ),
    ]
