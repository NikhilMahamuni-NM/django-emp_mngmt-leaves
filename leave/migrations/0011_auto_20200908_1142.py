# Generated by Django 3.0.3 on 2020-09-08 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leave', '0010_leave_leaves_avai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='leaves_avai',
            field=models.CharField(max_length=2),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaves_avai', models.CharField(max_length=2)),
                ('emp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
