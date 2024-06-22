# Generated by Django 5.0.6 on 2024-06-22 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('price', models.FloatField(verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='images/food/')),
                ('is_available', models.BooleanField(default=True, verbose_name='Is Available')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Username')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('address', models.CharField(max_length=50, verbose_name='Address')),
                ('userImage', models.ImageField(upload_to='images/profile/')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('total', models.FloatField(verbose_name='Total')),
                ('orderDate', models.DateTimeField(auto_now_add=True, verbose_name='Order Date')),
                ('is_delivered', models.BooleanField(default=False, verbose_name='Is Delivered')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
