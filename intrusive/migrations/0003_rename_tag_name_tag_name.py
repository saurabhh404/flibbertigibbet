# Generated by Django 5.0.6 on 2024-05-20 05:30
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("intrusive", "0002_rename_sidenotes_sidenote"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tag",
            old_name="tag_name",
            new_name="name",
        ),
    ]
