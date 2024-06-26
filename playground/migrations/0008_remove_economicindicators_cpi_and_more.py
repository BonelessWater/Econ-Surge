# Generated by Django 5.0.6 on 2024-05-22 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0007_economicindicators_indicator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='economicindicators',
            name='cpi',
        ),
        migrations.RemoveField(
            model_name='economicindicators',
            name='federal_funds_rate',
        ),
        migrations.RemoveField(
            model_name='economicindicators',
            name='inflation',
        ),
        migrations.RemoveField(
            model_name='economicindicators',
            name='real_gdp',
        ),
        migrations.RemoveField(
            model_name='economicindicators',
            name='real_gdp_per_capita',
        ),
        migrations.RemoveField(
            model_name='economicindicators',
            name='unemployment',
        ),
        migrations.AddField(
            model_name='economicindicators',
            name='value',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
