# Generated by Django 4.2.13 on 2024-07-02 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_product_support_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='copy_info',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='domain_info',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_info',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_images_info',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unique_design_info',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
