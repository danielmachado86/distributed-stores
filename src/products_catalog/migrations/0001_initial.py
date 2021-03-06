# Generated by Django 3.1.7 on 2021-04-20 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('picture', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('parent', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('picture', models.URLField(blank=True, null=True)),
            ],
            options={
                'unique_together': {('name', 'parent')},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('picture', models.URLField(blank=True, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_catalog.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_catalog.category')),
            ],
            options={
                'unique_together': {('name', 'brand')},
            },
        ),
        migrations.CreateModel(
            name='ProductSpecs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(max_length=30)),
                ('value', models.CharField(max_length=140)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_catalog.product')),
            ],
            options={
                'unique_together': {('product', 'attribute')},
            },
        ),
    ]
