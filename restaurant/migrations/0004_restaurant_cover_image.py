# Generated by Django 5.1.3 on 2025-03-07 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_restaurant_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='restaurants/cover_images/'),
        ),
    ]
