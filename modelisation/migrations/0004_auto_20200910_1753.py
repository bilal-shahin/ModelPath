# Generated by Django 3.0.3 on 2020-09-10 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelisation', '0003_auto_20200910_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genes',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('synonyms', models.TextField(blank=True, null=True)),
                ('bigg', models.CharField(blank=True, max_length=50, null=True)),
                ('asap', models.CharField(blank=True, max_length=50, null=True)),
                ('ncbi', models.CharField(blank=True, max_length=50, null=True)),
                ('uniprot', models.CharField(blank=True, max_length=50, null=True)),
                ('sbo', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('organism', models.CharField(max_length=255)),
                ('genes', models.ManyToManyField(to='modelisation.Genes')),
                ('metabolites', models.ManyToManyField(to='modelisation.Metabolites')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.RenameField(
            model_name='reaction_products',
            old_name='reaction_id',
            new_name='reaction',
        ),
        migrations.RenameField(
            model_name='reaction_substrates',
            old_name='reaction_id',
            new_name='reaction',
        ),
        migrations.AddField(
            model_name='reaction_products',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modelisation.Metabolites'),
        ),
        migrations.AddField(
            model_name='reaction_substrates',
            name='substrate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modelisation.Metabolites'),
        ),
        migrations.AlterField(
            model_name='reactions',
            name='ec_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='reaction_products',
            unique_together={('reaction', 'product')},
        ),
        migrations.AlterUniqueTogether(
            name='reaction_substrates',
            unique_together={('reaction', 'substrate')},
        ),
        migrations.CreateModel(
            name='Reaction_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lower_bound', models.FloatField(default=0.0)),
                ('upper_bound', models.FloatField(default=1000.0)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelisation.Model')),
                ('reaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelisation.Reactions')),
            ],
            options={
                'unique_together': {('reaction', 'model')},
            },
        ),
        migrations.AddField(
            model_name='model',
            name='reactions',
            field=models.ManyToManyField(related_name='reactions', through='modelisation.Reaction_model', to='modelisation.Reactions'),
        ),
        migrations.AddField(
            model_name='genes',
            name='reaction',
            field=models.ManyToManyField(blank=True, to='modelisation.Reactions'),
        ),
        migrations.RemoveField(
            model_name='reaction_products',
            name='metabolite_id',
        ),
        migrations.RemoveField(
            model_name='reaction_substrates',
            name='metabolite_id',
        ),
    ]
