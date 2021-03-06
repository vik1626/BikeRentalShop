# Generated by Django 3.2.12 on 2022-03-03 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'rbs_customer',
            },
        ),
        migrations.CreateModel(
            name='VehicleInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(max_length=50)),
                ('inventory_stock', models.IntegerField(default=0)),
                ('email_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'rbs_vehicle_inventory',
            },
        ),
        migrations.CreateModel(
            name='RentalMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.CharField(blank=True, max_length=30, null=True)),
                ('return_date', models.CharField(blank=True, max_length=30, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_rental_master', to='rbs.customer')),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_vehicle_inventory', to='rbs.vehicleinventory')),
            ],
            options={
                'db_table': 'rbs_rental_master',
            },
        ),
    ]
