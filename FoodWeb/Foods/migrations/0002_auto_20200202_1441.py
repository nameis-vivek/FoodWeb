# Generated by Django 3.0.2 on 2020-02-02 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='created',
        ),
        migrations.RemoveField(
            model_name='food',
            name='status',
        ),
        migrations.RemoveField(
            model_name='food',
            name='updated',
        ),
    ]