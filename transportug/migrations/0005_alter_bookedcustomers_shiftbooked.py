# Generated by Django 4.1.2 on 2022-12-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transportug", "0004_alter_bookedcustomers_bookingdate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookedcustomers",
            name="shiftBooked",
            field=models.DateTimeField(null=True),
        ),
    ]
