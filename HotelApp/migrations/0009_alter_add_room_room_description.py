# Generated by Django 4.1.3 on 2023-05-07 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("HotelApp", "0008_add_room_room_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="add_room",
            name="Room_Description",
            field=models.CharField(default="description", max_length=500),
        ),
    ]
