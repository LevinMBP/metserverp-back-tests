# Generated by Django 4.0 on 2024-03-09 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_alter_inventorytransaction_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawmaterials_inventorytransaction',
            name='m_quantity',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=16, null=True),
        ),
        migrations.AddField(
            model_name='rawmaterials_inventorytransaction',
            name='p_quantity',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=16, null=True),
        ),
    ]
