# Generated by Django 3.1.2 on 2021-02-11 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('climatic_condition', models.CharField(max_length=100)),
                ('water_quantity', models.CharField(max_length=100)),
                ('moisture', models.CharField(max_length=100)),
                ('pesticides', models.CharField(max_length=200)),
                ('ph_level', models.FloatField(default=0)),
                ('min_temp', models.FloatField(default=0)),
                ('max_temp', models.FloatField(default=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]