# Generated by Django 2.0.3 on 2018-09-04 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0003_auto_20180903_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='badge_number',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
