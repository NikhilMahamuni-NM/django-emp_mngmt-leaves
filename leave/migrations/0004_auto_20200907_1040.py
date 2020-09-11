# Generated by Django 3.0.3 on 2020-09-07 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_leave'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='approval',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='leave',
            name='approval_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='leave',
            name='approved_by',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]