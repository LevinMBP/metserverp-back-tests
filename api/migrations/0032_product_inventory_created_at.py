# Generated by Django 4.0 on 2024-03-10 21:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_sales_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_inventory',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
