# Generated by Django 3.0.3 on 2020-09-07 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leave', '0007_auto_20200907_1105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave',
            old_name='emp_name',
            new_name='full_name',
        ),
        migrations.AddField(
            model_name='leave',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
