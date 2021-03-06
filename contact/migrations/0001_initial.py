# Generated by Django 3.0.2 on 2020-01-31 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetInTouch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('message', models.TextField(blank=True, db_index=True)),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('email', models.EmailField(max_length=30)),
                ('notes', models.TextField(blank=True, db_index=True)),
                ('treatment_needed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aboutus.DoctorProfile')),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
            },
        ),
    ]
