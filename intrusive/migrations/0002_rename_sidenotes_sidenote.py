# Generated by Django 5.0.6 on 2024-05-17 10:54
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("intrusive", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SideNotes",
            new_name="SideNote",
        ),
    ]