# Generated by Django 5.1.3 on 2024-11-25 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0002_rename_profile_pic_customuser_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='profile_picture',
            new_name='profile_pic',
        ),
    ]
