# Generated by Django 5.1.2 on 2024-12-16 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0004_alter_transaction_date_alter_transaction_montant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('expense', 'Depense'), ('income', 'Revenu')], max_length=20),
        ),
    ]
