# Generated by Django 4.1.2 on 2022-10-28 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transportug', '0002_remove_buscompany_busimage_bus_busimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='busImage',
        ),
    ]
