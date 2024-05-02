# Generated by Django 4.0 on 2024-03-02 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_sales_tax_percent'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_invoice', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='sales',
            name='salesInvoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.salesinvoice'),
        ),
    ]
