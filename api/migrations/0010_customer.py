# Generated by Django 4.0 on 2023-12-09 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_product_inventory_options_alter_unit_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50, unique=True)),
                ('contact_person', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=10, null=True)),
                ('company_address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
