# Generated by Django 4.1.3 on 2023-05-16 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("HotelApp", "0011_alter_add_room_room_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="online_booking",
            name="Room_Id",
            field=models.ForeignKey(
                default=4,
                on_delete=django.db.models.deletion.CASCADE,
                to="HotelApp.add_room",
            ),
            preserve_default=False,
        ),
    ]
