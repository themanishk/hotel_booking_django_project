# Generated by Django 2.2.6 on 2019-11-08 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20191108_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='photo',
            field=models.ImageField(default=0, upload_to='pics'),
        ),
    ]
