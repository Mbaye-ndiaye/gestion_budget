# Generated by Django 5.1.2 on 2024-12-16 14:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('budget', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='budget', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('transaction_type', models.CharField(choices=[('expenseDepenseincome', 'Revenue')], max_length=20)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transation', to='gestionapp.budget')),
            ],
        ),
    ]
