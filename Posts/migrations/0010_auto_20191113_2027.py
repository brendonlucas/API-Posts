# Generated by Django 2.2.6 on 2019-11-13 23:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0009_auto_20191113_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
