# Generated by Django 4.0.3 on 2022-03-24 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('signid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
