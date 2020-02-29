from django.conf import settings
from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Auction(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=0)
    image = models.ImageField(upload_to='images')
    

    def __str__(self):
        return self.name