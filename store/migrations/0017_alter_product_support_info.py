# Generated by Django 4.2.13 on 2024-07-02 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_remove_product_information_product_copy_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='support_info',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
