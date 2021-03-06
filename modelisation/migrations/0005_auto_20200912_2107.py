# Generated by Django 3.0.3 on 2020-09-12 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelisation', '0004_auto_20200910_1753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genes',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='metabolites',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='reactions',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='model',
            name='nb_metabolites',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='model',
            name='nb_reactions',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='model',
            name='objective',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='metabolites',
            name='compartment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
