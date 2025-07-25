# Generated by Django 5.2.1 on 2025-07-21 09:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGoogleTokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=255, verbose_name='Google Access Token')),
                ('refresh_token', models.CharField(blank=True, max_length=255, null=True, verbose_name='Google Refresh Token')),
                ('expires_in', models.DateTimeField(verbose_name='Access Token Expiry Time')),
                ('token_type', models.CharField(default='Bearer', max_length=50, verbose_name='Token Type')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Updated At')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='google_tokens', to=settings.AUTH_USER_MODEL, verbose_name='Django User')),
            ],
            options={
                'verbose_name': 'User Google Token',
                'verbose_name_plural': 'User Google Tokens',
            },
        ),
    ]
