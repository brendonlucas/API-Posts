# Generated by Django 2.2.6 on 2019-11-16 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0011_auto_20191113_2053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='userId',
            new_name='profile',
        ),
    ]
