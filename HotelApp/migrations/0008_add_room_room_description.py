# Generated by Django 4.1.3 on 2023-05-07 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("HotelApp", "0007_add_salarys"),
    ]

    operations = [
        migrations.AddField(
            model_name="add_room",
            name="Room_Description",
            field=models.CharField(default="", max_length=500),
        ),
    ]
