# Generated by Django 3.0.7 on 2020-06-14 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meto_user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('staff_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=255)),
                ('staff_phone', models.CharField(max_length=255, unique=True)),
                ('staff_area', models.CharField(max_length=255)),
                ('staff_city', models.CharField(max_length=255)),
                ('staff_pincode', models.CharField(max_length=255)),
                ('staff_job_status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='worker',
            fields=[
                ('worker_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('worker_name', models.CharField(max_length=255)),
                ('worker_phone', models.CharField(max_length=255, unique=True)),
                ('worker_area', models.CharField(max_length=255)),
                ('worker_city', models.CharField(max_length=255)),
                ('worker_pincode', models.CharField(max_length=255)),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meto_user_app.service')),
            ],
        ),
    ]
