# Generated by Django 3.1.7 on 2021-04-14 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scientific', '0009_delete_myproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('place', models.TextField()),
                ('date', models.TextField()),
            ],
        ),
    ]