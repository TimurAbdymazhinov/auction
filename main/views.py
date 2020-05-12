from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from category.models import Category
from auctioncore.models import Auction
from banner.models import Banner


class MainView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        # Category
        category = Category.objects.all().order_by('order')
        a = Auction.objects.all()
        b = Banner.objects.all()
        return render(request, self.template_name, context={
            "category": category,
            "auctions": a,
            "banners": b,

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
