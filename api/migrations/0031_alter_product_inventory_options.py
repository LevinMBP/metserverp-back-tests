# Generated by Django 4.0 on 2023-12-18 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_alter_product_inventory_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product_inventory',
            options={'ordering': ['ordered_date'], 'verbose_name_plural': 'Product Inventories'},
        ),
    ]
