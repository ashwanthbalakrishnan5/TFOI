# Generated by Django 4.2.1 on 2023-08-29 16:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("poll", "0005_alter_boothdata2014_arun_ajabrao_pachare_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="boothdata2014",
            name="no_of_tendered_votes",
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
