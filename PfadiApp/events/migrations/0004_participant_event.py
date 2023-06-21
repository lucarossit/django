# Generated by Django 4.2 on 2023-06-16 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_participant'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='event',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='events.event'),
            preserve_default=False,
        ),
    ]
