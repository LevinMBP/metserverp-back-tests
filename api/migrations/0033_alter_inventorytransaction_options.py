# Generated by Django 4.0 on 2023-12-18 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_inventorytransaction_transaction_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventorytransaction',
            options={'ordering': ['transaction_date']},
        ),
    ]
