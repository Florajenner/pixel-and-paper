from django.db import models

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    file = models.FileField(upload_to='downloads/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
