# Generated by Django 5.2.1 on 2025-07-24 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('connection_request_received', 'Connection Request Received'), ('connection_request_accepted', 'Connection Request Accepted'), ('connection_request_cancelled', 'Connection Request Cancelled'), ('session_cancelled', 'Session Cancelled')], max_length=50),
        ),
    ]
