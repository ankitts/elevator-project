# Generated by Django 4.2.2 on 2023-06-16 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0009_elevator_max_floor"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="elevator",
            name="running",
        ),
    ]