# Generated by Django 4.0.6 on 2022-12-21 12:30

from django.db import migrations, models

#models.py içeriği migrate edildikten sonra oluşturulan yer burası, yani önce modeller olmalı.


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basvuru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('surname', models.CharField(blank=True, max_length=30)),
                ('tckimlik', models.CharField(blank=True, max_length=11, unique=True)),
                ('telefon', models.CharField(blank=True, max_length=30)),
                ('tecrübe', models.CharField(blank=True, max_length=50)),
                ('message', models.CharField(blank=True, max_length=30)),
                ('confirmed', models.BooleanField(default=False, verbose_name='Durum')),
                ('posta', models.EmailField(blank=True, max_length=254)),
                ('bolum', models.CharField(choices=[('SPO', 'Spor'), ('FEN', 'Fen Bilimleri'), ('MUH', 'Mühendislik')], default='MUH', max_length=3)),
                ('cinsiyet', models.CharField(choices=[('e', 'Erkek'), ('h', 'Kadın'), ('b', 'Belirtmek istemiyorum')], default='b', max_length=11)),
            ],
        ),
    ]