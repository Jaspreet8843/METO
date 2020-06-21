# Generated by Django 3.0.7 on 2020-06-20 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meto_user_app', '0005_auto_20200619_1235'),
        ('meto_admin_app', '0006_auto_20200619_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='assign_staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meto_user_app.booking')),
                ('staff_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meto_admin_app.staff')),
            ],
        ),
        migrations.CreateModel(
            name='assign_worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meto_user_app.booking')),
                ('worker_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meto_admin_app.worker')),
            ],
        ),
        migrations.DeleteModel(
            name='assign',
        ),
    ]