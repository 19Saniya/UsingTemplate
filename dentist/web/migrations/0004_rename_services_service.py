# Generated by Django 4.2.5 on 2023-10-08 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_services'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
    ]