# Generated by Django 4.0 on 2024-05-12 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0053_alter_inventorytransaction_inventory_pk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='sales_transaction',
            field=models.ManyToManyField(through='api.InventoryTransaction', to='api.Product_Inventory'),
        ),
    ]
