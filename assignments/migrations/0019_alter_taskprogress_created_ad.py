# Generated by Django 4.1.1 on 2022-09-16 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0018_alter_taskprogress_created_ad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskprogress',
            name='created_ad',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]