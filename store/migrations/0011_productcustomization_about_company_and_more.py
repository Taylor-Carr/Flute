# Generated by Django 4.2.13 on 2024-06-07 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_remove_productcustomization_product_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcustomization',
            name='about_company',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productcustomization',
            name='areas_covered',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productcustomization',
            name='company_established',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productcustomization',
            name='industry',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productcustomization',
            name='reference_website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productcustomization',
            name='services',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productcustomization',
            name='target_market',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
