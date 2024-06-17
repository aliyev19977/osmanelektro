# Generated by Django 4.2.13 on 2024-06-17 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0002_category_slug_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='about',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]