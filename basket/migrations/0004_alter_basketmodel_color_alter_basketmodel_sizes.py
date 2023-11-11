# Generated by Django 4.2.3 on 2023-10-03 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_productmodel_quantity'),
        ('basket', '0003_remove_basketmodel_ammount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketmodel',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productcolormodel'),
        ),
        migrations.AlterField(
            model_name='basketmodel',
            name='sizes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productsizemodel'),
        ),
    ]
