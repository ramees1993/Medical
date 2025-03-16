# Generated by Django 5.0.4 on 2025-03-15 00:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_newslettersubscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=100)),
                ('disease', models.CharField(max_length=50)),
                ('booked', models.DateField()),
                ('time', models.TimeField()),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.doctor')),
            ],
            options={
                'verbose_name': 'Patients',
                'verbose_name_plural': 'Patients',
            },
        ),
    ]
