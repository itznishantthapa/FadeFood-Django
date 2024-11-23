# Generated by Django 5.1.3 on 2024-11-23 01:07

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
            name='restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('business_type', models.CharField(max_length=100)),
                ('opening_hour', models.CharField(blank=True, max_length=10, null=True)),
                ('logo', models.ImageField(blank=True, upload_to='restaurant_logo/')),
                ('is_active', models.BooleanField(default=False)),
                ('restaurant_images', models.ImageField(blank=True, upload_to='restaurant_images/')),
                ('rating', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('latitude', models.FloatField(default=0.0)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]