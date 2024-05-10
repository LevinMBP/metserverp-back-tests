# Generated by Django 4.0 on 2024-05-10 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0050_alter_inventorytransaction_sales_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorytransaction',
            name='inventory_pk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='invtrans', to='api.product_inventory'),
        ),
    ]