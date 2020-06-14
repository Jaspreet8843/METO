# Generated by Django 3.0.7 on 2020-06-14 08:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('booking_date', models.DateField(default=django.utils.timezone.now)),
                ('booking_desc', models.CharField(blank=True, max_length=255)),
                ('booking_phone', models.CharField(max_length=255)),
                ('booking_area', models.CharField(max_length=255)),
                ('booking_city', models.CharField(max_length=255)),
                ('booking_pincode', models.CharField(max_length=255)),
                ('booking_status', models.CharField(default='Processing', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='dates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField()),
                ('staff_assigned_date', models.DateField()),
                ('technician_assigned_date', models.DateField()),
                ('technician_visited_date', models.DateField()),
                ('close_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=255)),
                ('service_status', models.CharField(default='Available', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255)),
                ('user_password', models.CharField(max_length=255)),
                ('user_dp', models.CharField(blank=True, max_length=255)),
                ('user_email', models.CharField(max_length=255, unique=True)),
                ('user_phone', models.CharField(max_length=255, unique=True)),
                ('user_gender', models.CharField(blank=True, max_length=255)),
                ('user_area', models.CharField(blank=True, max_length=255)),
                ('user_city', models.CharField(blank=True, max_length=255)),
                ('user_pincode', models.CharField(blank=True, max_length=255)),
                ('user_since', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
