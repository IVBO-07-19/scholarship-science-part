# Generated by Django 3.1.7 on 2021-03-31 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Scientific', '0004_auto_20210331_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myproject',
            name='nameProject',
        ),
    ]
