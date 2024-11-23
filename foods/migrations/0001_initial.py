# Generated by Django 5.1.3 on 2024-11-23 02:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0002_alter_restaurant_logo_alter_restaurant_owner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(blank=True, max_length=100, null=True)),
                ('food_price', models.FloatField(blank=True, default=0.0, null=True)),
                ('food_image', models.ImageField(blank=True, null=True, upload_to='food_images/')),
                ('rating', models.FloatField(blank=True, default=0.0, null=True)),
                ('reviews', models.IntegerField(default=0)),
                ('is_available', models.BooleanField(default=True)),
                ('totol_eats', models.IntegerField(default=0)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('restaurant_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
    ]