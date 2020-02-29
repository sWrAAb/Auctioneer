from django.db import models
from django.contrib.auth.models import User
from auctions.models import Auction

# Create your models here.

class Bidding(models.Model):
    