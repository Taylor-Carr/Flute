# Generated by Django 4.2.13 on 2024-07-02 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_benefit_remove_product_benefits_product_benefits'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='information',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='plan',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
