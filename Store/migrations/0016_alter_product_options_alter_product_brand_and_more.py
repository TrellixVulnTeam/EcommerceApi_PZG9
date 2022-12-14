# Generated by Django 4.1 on 2022-08-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0015_alter_product_brand'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('Nike', 'Nike'), ('Dior', 'Dior'), ('Adidas', 'Adidas'), ('Under Armour', 'Under Armour'), ('H&M', 'H And M'), ('Zara', 'Zara'), ('Polo', 'Polo'), ('Levis', 'Levis')], default='Dior', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], default='L', max_length=20),
        ),
    ]
