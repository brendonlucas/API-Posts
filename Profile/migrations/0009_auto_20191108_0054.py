# Generated by Django 2.2.6 on 2019-11-08 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0008_auto_20191108_0049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='address',
        ),
    ]
