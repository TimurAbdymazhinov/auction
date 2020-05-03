from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Auction


class AuctionDeleteView(TemplateView):

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        a = Auction.objects.get(pk=id).delete()

        return redirect('profile')
