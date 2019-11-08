# Generated by Django 2.2.6 on 2019-10-31 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('body', models.CharField(max_length=200)),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Posts.Post')),
            ],
        ),
    ]
