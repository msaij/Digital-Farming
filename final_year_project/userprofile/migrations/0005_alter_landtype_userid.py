# Generated by Django 3.2 on 2021-05-11 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20210511_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landtype',
            name='userid',
            field=models.CharField(max_length=20),
        ),
    ]