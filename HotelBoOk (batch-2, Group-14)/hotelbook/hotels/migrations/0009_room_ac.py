# Generated by Django 2.2.6 on 2019-11-08 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0008_auto_20191108_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='ac',
            field=models.BooleanField(default=False),
        ),
    ]
