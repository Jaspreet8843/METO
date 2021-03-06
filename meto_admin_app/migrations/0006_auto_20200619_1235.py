# Generated by Django 3.0.7 on 2020-06-19 07:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meto_admin_app', '0005_staff_staff_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='visiting_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 6, 19, 7, 5, 35, 58215, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='date',
            name='booking_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='date',
            name='close_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='date',
            name='staff_assigned_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='date',
            name='technician_assigned_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='date',
            name='technician_visited_date',
            field=models.DateField(blank=True),
        ),
    ]
