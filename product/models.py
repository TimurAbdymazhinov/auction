from django.db import models
from auctioncore.models import Auction


# Create your models here.

class Product(models.Model):
    auction = models.OneToOneField(Auction, on_delete=models.CASCADE, related_name='lot')

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.title
