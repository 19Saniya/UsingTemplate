# Generated by Django 4.2.5 on 2023-10-08 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_rename_service_serviceheading_service_heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavbarHeading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navbar_heading', models.CharField(max_length=255)),
            ],
        ),
    ]
