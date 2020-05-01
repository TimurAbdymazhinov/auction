from django.contrib.auth.models import User
from django.db import models
from category.models import Category


class Auction(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auctions')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='auctions')

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=200, verbose_name='Страна', null=True, blank=True)
    city = models.CharField(max_length=200, verbose_name='Город', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_done = models.BooleanField(default=False)

    start_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.title


class Participants(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participants')
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='participants')
    # stavka = models.DateField()
