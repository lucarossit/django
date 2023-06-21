# Generated by Django 4.2 on 2023-05-26 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.IntegerField(default=0),
        ),
    ]
