# Generated by Django 2.0.3 on 2018-09-04 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0004_auto_20180903_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkin',
            name='guest',
        ),
        migrations.AddField(
            model_name='guest',
            name='is_checked_in',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Checkin',
        ),
    ]
