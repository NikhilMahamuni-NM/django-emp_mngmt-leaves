# Generated by Django 3.0.3 on 2020-09-07 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0006_leave'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='applied_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='leave',
            name='remark',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
