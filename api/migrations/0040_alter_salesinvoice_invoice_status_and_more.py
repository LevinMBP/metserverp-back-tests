# Generated by Django 4.0 on 2024-03-18 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_remove_sales_sales_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesinvoice',
            name='invoice_status',
            field=models.CharField(blank=True, choices=[('UNPAID', 'UNPAID'), ('PAID', 'PAID')], default='UNPAID', max_length=6),
        ),
        migrations.AlterField(
            model_name='salesinvoice',
            name='sales_invoice',
            field=models.CharField(blank=True, default='', max_length=150, unique=True),
        ),
    ]
