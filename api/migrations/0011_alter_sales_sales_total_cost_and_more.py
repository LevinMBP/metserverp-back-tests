# Generated by Django 4.0 on 2024-02-23 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_sales_sales_margin_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='sales_total_cost',
            field=models.DecimalField(decimal_places=2, max_digits=24),
        ),
        migrations.AlterField(
            model_name='sales',
            name='sales_unit_cost',
            field=models.DecimalField(decimal_places=2, max_digits=18),
        ),
    ]
