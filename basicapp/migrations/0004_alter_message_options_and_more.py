# Generated by Django 5.0.1 on 2024-01-20 14:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("basicapp", "0003_alter_room_options_room_patricipants"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="message",
            options={"ordering": ["-updated", "-created"]},
        ),
        migrations.RenameField(
            model_name="room",
            old_name="patricipants",
            new_name="participants",
        ),
    ]
