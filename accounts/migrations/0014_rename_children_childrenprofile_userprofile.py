# Generated by Django 4.1.1 on 2022-09-23 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0020_alter_childrencourserelation_created_ad'),
        ('accounts', '0013_alter_allscore_kid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Children',
            new_name='ChildrenProfile',
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=50)),
                ('phone_numbers', models.IntegerField()),
                ('age', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]