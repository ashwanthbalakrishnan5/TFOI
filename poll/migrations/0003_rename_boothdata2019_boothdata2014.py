# Generated by Django 4.2.1 on 2023-08-29 16:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("poll", "0002_boothdata2019"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="BoothData2019",
            new_name="BoothData2014",
        ),
    ]
