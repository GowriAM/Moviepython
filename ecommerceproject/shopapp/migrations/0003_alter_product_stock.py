# Generated by Django 4.1 on 2024-02-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopapp", "0002_cart_rename_descriptio_category_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="stock",
            field=models.IntegerField(),
        ),
    ]
