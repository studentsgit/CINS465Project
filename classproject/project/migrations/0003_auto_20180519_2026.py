# Generated by Django 2.0.2 on 2018-05-20 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_restaurant_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='stateOrProvince',
            new_name='State',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='country',
        ),
    ]
