# Generated by Django 4.2 on 2023-06-21 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_participant_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='participants',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='event',
        ),
        migrations.AddField(
            model_name='participant',
            name='event',
            field=models.ManyToManyField(to='events.event'),
        ),
    ]
