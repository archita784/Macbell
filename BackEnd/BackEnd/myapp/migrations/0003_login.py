# Generated by Django 3.0.8 on 2020-07-11 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200711_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('userid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('usertype', models.CharField(max_length=20)),
            ],
        ),
    ]