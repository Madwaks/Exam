# Generated by Django 3.0.5 on 2020-12-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("teacher", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="salary",
            field=models.PositiveIntegerField(null=True),
        )
    ]
