
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from category.models import Category
from auctioncore.models import Auction

class MainView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        # Category
        category = Category.objects.filter(owner=None)
        a = Auction.objects.all()
        return render(request, self.template_name, context={
            "category": category,
            "auctions": a,

        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

class TempView(TemplateView):
    template_name = 'main/products.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, context={
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })
