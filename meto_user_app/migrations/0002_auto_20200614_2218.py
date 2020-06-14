# Generated by Django 3.0.7 on 2020-06-14 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meto_admin_app', '0001_initial'),
        ('meto_user_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='worker_id',
        ),
        migrations.CreateModel(
            name='assign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='meto_user_app.booking')),
                ('staff_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='meto_admin_app.staff')),
                ('worker_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='worker', to='meto_admin_app.worker')),
            ],
        ),
    ]