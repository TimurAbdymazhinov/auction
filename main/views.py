from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from category.models import Category
from auctioncore.models import Auction
from banner.models import Banner
from auctioncore.tools import is_time_out

class MainView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        # Category
        category = Category.objects.all().order_by('order')
        is_time_out()
        a = Auction.objects.filter(is_active=True)

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
