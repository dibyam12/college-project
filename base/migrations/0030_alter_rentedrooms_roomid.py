# Generated by Django 5.0.7 on 2024-11-30 06:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_remove_rentedrooms_rented_rentedrooms_rent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentedrooms',
            name='roomId',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.roomdetails'),
        ),
    ]
