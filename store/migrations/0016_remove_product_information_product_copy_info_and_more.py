# Generated by Django 4.2.13 on 2024-07-02 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_product_information_alter_product_plan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='information',
        ),
        migrations.AddField(
            model_name='product',
            name='copy_info',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='domain_info',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='seo_info',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_images_info',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='support_info',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='unique_design_info',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]