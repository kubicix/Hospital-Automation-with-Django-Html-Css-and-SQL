# Generated by Django 4.1.3 on 2023-04-29 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hasta',
            fields=[
                ('tcno', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]