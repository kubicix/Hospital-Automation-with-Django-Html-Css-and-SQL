# Generated by Django 4.1.3 on 2023-05-04 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_rename_bolum_adi_bolum_bolumad_remove_bolum_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Randevu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarih', models.DateField()),
                ('saat', models.TimeField()),
                ('bolum', models.CharField(max_length=255)),
            ],
        ),
    ]
