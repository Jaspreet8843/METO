# Generated by Django 3.0.7 on 2020-06-13 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meto_user_app', '0001_initial'),
        ('meto_admin_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='service_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meto_user_app.service'),
        ),
    ]
