# Generated by Django 4.1.1 on 2022-09-14 11:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0005_taskprogress_created_ad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskprogress',
            name='created_ad',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 14, 14, 0, 14, 13747)),
        ),
    ]
