# Generated by Django 3.0.3 on 2020-09-13 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelisation', '0008_auto_20200913_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactions',
            name='ec_number',
            field=models.TextField(blank=True, null=True),
        ),
    ]
