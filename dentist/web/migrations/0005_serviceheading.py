# Generated by Django 4.2.5 on 2023-10-08 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_rename_services_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceHeading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=255)),
            ],
        ),
    ]
