# Generated by Django 3.0.7 on 2020-06-14 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meto_admin_app', '0002_worker_service_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staff_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='worker',
            name='worker_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
