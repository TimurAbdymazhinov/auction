from django.contrib import admin
from .models import Auction


class AuctionAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


admin.site.register(Auction, AuctionAdmin)
