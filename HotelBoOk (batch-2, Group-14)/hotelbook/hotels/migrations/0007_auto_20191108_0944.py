# Generated by Django 2.2.6 on 2019-11-08 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_auto_20191108_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='parking',
        ),
        migrations.RemoveField(
            model_name='room',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='room',
            name='pools',
        ),
        migrations.RemoveField(
            model_name='room',
            name='smart_tv',
        ),
        migrations.RemoveField(
            model_name='room',
            name='wifi',
        ),
    ]
