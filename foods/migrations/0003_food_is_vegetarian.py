# Generated by Django 5.1.3 on 2025-03-08 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_remove_food_category_remove_food_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='is_vegetarian',
            field=models.BooleanField(default=False),
        ),
    ]
