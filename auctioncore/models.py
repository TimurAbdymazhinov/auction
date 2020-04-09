from django.contrib.auth.models import User
from django.db import models
from category.models import Category


class Auction(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auctions')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='auctions')

    is_client = models.BooleanField(default=False)
    is_auction_owner = models.BooleanField(default=False)
    title = models
    country = models.CharField(max_length=200, verbose_name='Страна', null=True, blank=True)
    city = models.CharField(max_length=200, verbose_name='Город', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return
