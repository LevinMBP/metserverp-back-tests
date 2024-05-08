# Generated by Django 4.0 on 2024-05-01 01:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_alter_sales_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rawmaterials_inventory',
            options={'ordering': ['ordered_date', 'created_at', 'pk'], 'verbose_name_plural': 'Raw Material Inventories'},
        ),
        migrations.AddField(
            model_name='rawmaterials_inventory',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]