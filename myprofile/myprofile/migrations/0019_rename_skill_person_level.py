# Generated by Django 5.0.6 on 2024-06-22 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0018_rename_images_person_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='skill',
            new_name='level',
        ),
    ]
