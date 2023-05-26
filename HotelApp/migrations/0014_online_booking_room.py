# Generated by Django 4.1.3 on 2023-05-16 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("HotelApp", "0013_remove_online_booking_room_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="online_booking",
            name="room",
            field=models.ForeignKey(
                # default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="HotelApp.add_room",
            ),
            preserve_default=False,
        ),
    ]