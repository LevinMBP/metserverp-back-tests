# Generated by Django 4.0 on 2024-03-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_alter_product_inventory_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesinvoice',
            name='sales_invoice',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
    ]