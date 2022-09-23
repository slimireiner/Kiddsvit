# Generated by Django 4.1.1 on 2022-09-19 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_user_email_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='children',
            name='children_profile',
        ),
        migrations.AddField(
            model_name='children',
            name='children_user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='children_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
