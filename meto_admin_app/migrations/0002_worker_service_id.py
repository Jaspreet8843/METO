# Generated by Django 3.0.7 on 2020-06-14 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meto_user_app', '0002_auto_20200614_2218'),
        ('meto_admin_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='service_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meto_user_app.service'),
        ),
    ]
