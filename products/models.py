from django.conf import settings
from django.db import models
from django.shortcuts import reverse

# Create your models here.

CATEGORY_CHOICES = (
    ('C','Clothes'),
    ('Fw','Footwear'),
    ('Te','Technology'),
    ('Ty','Toys'),
    ('To','Tools'),
    ('Od','Outdoors'),
    ('Pe','Pets'),
    ('Ve','Vehicles'),
)


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, default='C')
    slug = models.SlugField(max_length=100, default='product-')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})