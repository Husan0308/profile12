# Generated by Django 5.0.6 on 2024-07-18 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0037_remove_person_customer_alter_person_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
    ]
