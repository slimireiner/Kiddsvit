# Generated by Django 4.1.1 on 2022-09-16 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0010_taskprogress_finished_ad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskprogress',
            name='created_ad',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 16, 12, 27, 17, 886483)),
        ),
    ]
