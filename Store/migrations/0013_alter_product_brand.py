# Generated by Django 4.1 on 2022-08-21 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0012_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('Nike', 'Nike'), ('Dior', 'Dior'), ('Adidas', 'Adidas'), ('Polo', 'Polo')], max_length=20),
        ),
    ]
