from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from category.models import Category
from auctioncore.models import Auction
from banner.models import Banner, Page
from auctioncore.tools import is_time_out

class MainView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        # Category
        category = Category.objects.all().order_by('order')
        is_time_out()
        a = Auction.objects.filter(is_active=True)
        da = Auction.objects.filter(is_active=False)

        b = Banner.objects.all()
        dpage = Page.objects.filter(is_active=True)
        return render(request, self.template_name, context={
            "category": category,
            "auctions": a,
            "banners": b,
            "done_auctions": da,
            "dpage": dpage

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
