# Generated by Django 4.0 on 2023-12-18 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_alter_sales_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sales',
            options={'verbose_name_plural': 'Sales'},
        ),
    ]
