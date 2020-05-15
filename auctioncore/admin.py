from django.contrib import admin
from .models import Auction, Participants


class AuctionAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ['bet']
    search_fields = ['bet']


admin.site.register(Auction, AuctionAdmin)
admin.site.register(Participants, ParticipantsAdmin)
