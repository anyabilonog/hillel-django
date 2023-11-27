# Generated by Django 4.2.7 on 2023-11-27 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_storeinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stores',
            field=models.ManyToManyField(through='products.StoreInventory', to='products.store'),
        ),
        migrations.AddField(
            model_name='store',
            name='products',
            field=models.ManyToManyField(through='products.StoreInventory', to='products.product'),
        ),
        migrations.AddField(
            model_name='storeinventory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AlterField(
            model_name='storeinventory',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]