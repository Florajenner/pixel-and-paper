# Generated by Django 5.1.3 on 2024-11-25 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_category_product_image_alter_product_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='file',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='dimensions',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='downloadable_file',
            field=models.FileField(blank=True, null=True, upload_to='digital_downloads/'),
        ),
        migrations.AddField(
            model_name='product',
            name='file_format',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='preview_image',
            field=models.ImageField(blank=True, null=True, upload_to='preview_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('abstract', 'Abstract Art'), ('nature', 'Nature & Landscapes'), ('typography', 'Typography'), ('minimalist', 'Minimalist'), ('geometric', 'Geometric')], max_length=100),
        ),
    ]