# Generated by Django 4.2.13 on 2024-05-28 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_product_image_alter_productimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/category_images/'),
        ),
    ]