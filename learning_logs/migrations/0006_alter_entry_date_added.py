# Generated by Django 4.2.6 on 2023-10-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("learning_logs", "0005_alter_entry_date_added"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="date_added",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
