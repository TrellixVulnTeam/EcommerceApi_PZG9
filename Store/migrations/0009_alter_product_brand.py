# Generated by Django 4.1 on 2022-08-20 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0008_alter_brand_id_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_brand', to='Store.brand'),
        ),
    ]
