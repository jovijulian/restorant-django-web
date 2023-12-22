# Generated by Django 5.0 on 2023-12-20 06:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=100, null=True)),
                ('menu_price', models.FloatField(null=True)),
                ('menu_description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.CharField(max_length=5, null=True)),
                ('table_capacity', models.IntegerField(null=True)),
                ('table_status', models.CharField(max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
                ('username', models.CharField(max_length=40, null=True)),
                ('email', models.CharField(max_length=40, null=True)),
                ('password', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('ingredients', models.TextField(null=True)),
                ('directive', models.TextField(null=True)),
                ('menu_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(null=True)),
                ('grand_total', models.FloatField(null=True)),
                ('payment_method', models.CharField(max_length=20, null=True)),
                ('order_status', models.CharField(max_length=20, null=True)),
                ('menu_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.menu')),
                ('table_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.table')),
            ],
        ),
    ]