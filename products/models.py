from django.db import models

class Product(models.Model):
    CATEGORIES = [
        ('abstract', 'Abstract Art'),
        ('nature', 'Nature & Landscapes'),
        ('typography', 'Typography'),
        ('minimalist', 'Minimalist'),
        ('geometric', 'Geometric')
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    preview_image = models.ImageField(upload_to='preview_images/', null=True, blank=True)
    downloadable_file = models.FileField(upload_to='digital_downloads/', null=True, blank=True)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=100, choices=CATEGORIES)
    dimensions = models.CharField(max_length=100, null=True, blank=True)
    file_format = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title