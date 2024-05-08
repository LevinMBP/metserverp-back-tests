# Generated by Django 4.0 on 2024-02-14 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_product_inventory_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorytransaction',
            name='inventory_pk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.product_inventory'),
        ),
        migrations.AlterField(
            model_name='inventorytransaction',
            name='sales_pk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.sales'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(blank=True, choices=[('MANUFACTURED', 'MANUFACTURED'), ('IMPORTED', 'IMPORTED'), ('LOCAL PURCHASE', 'LOCAL PURCHASE')], default='', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='rawmaterials_inventory',
            name='material_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.rawmaterials'),
        ),
        migrations.AlterField(
            model_name='rawmaterials_inventory',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.supplier'),
        ),
        migrations.AlterField(
            model_name='rawmaterials_inventorytransaction',
            name='materials_inventory_pk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.rawmaterials_inventory'),
        ),
        migrations.AlterField(
            model_name='rawmaterials_inventorytransaction',
            name='product_inventory_pk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.product_inventory'),
        ),
        migrations.AlterField(
            model_name='rawmaterials_product',
            name='materials',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.rawmaterials'),
        ),
        migrations.AlterField(
            model_name='rawmaterials_product',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.product'),
        ),
    ]