# Generated by Django 4.2.7 on 2023-11-27 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_storeinventory_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeinventory',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
