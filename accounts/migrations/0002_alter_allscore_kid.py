# Generated by Django 4.1.1 on 2022-09-11 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allscore',
            name='kid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children_score', to='accounts.children'),
        ),
    ]
