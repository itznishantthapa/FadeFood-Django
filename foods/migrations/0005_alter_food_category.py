# Generated by Django 5.1.3 on 2024-11-25 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
