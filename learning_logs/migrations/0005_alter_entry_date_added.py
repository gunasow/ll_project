# Generated by Django 4.2.6 on 2023-10-30 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("learning_logs", "0004_topic_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry", name="date_added", field=models.DateTimeField(),
        ),
    ]
