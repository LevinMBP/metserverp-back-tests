# Generated by Django 4.0 on 2024-03-01 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_remove_sales_tax_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='tax_percent',
            field=models.DecimalField(blank=True, decimal_places=3, default=12, max_digits=6, null=True),
        ),
    ]
