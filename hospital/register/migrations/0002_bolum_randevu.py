# Generated by Django 4.1.3 on 2023-05-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bolum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bolum_adi', models.CharField(max_length=100)),
            ],
        ),
    ]