# Generated by Django 4.1.7 on 2023-03-16 20:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dealership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dealer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Make', to='cars_app.dealership')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2023)])),
                ('color', models.CharField(max_length=11)),
                ('make_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Type', to='cars_app.make')),
            ],
        ),
    ]
