# Generated by Django 5.2.3 on 2025-06-22 20:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CCTVArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PoliceStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CCTV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camera_no', models.PositiveIntegerField(blank=True, null=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
                ('last_ping', models.DateTimeField(blank=True, null=True)),
                ('thumbnail_url', models.URLField(blank=True, null=True)),
                ('cctv_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cctvs', to='monitoring.cctvarea')),
            ],
        ),
        migrations.AddField(
            model_name='cctvarea',
            name='police_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='monitoring.policestation'),
        ),
    ]
