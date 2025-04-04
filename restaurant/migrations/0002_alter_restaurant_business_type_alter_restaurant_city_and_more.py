# Generated by Django 5.1.3 on 2024-11-25 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='business_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='restaurants/logos/'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='street_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
