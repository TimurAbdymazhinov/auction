from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Auction, Participants, Acomments
from django.contrib.auth.mixins import LoginRequiredMixin
from category.models import Category
from auction.settings import LOGIN_URL
from .forms import AuctionForm
from product.forms import ProductForm
from product.models import ImageModel


class AuctionDeleteView(LoginRequiredMixin, TemplateView):
    login_url = LOGIN_URL

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        Auction.objects.get(pk=id).delete()

        return redirect('profile')


class AuctionEditView(LoginRequiredMixin, TemplateView):
    template_name = 'auctioncore/auction_edit.html'
    login_url = LOGIN_URL

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        category = Category.objects.filter(owner=None)
        auction = Auction.objects.get(pk=id)
        a = AuctionForm(instance=auction)
        p = ProductForm(instance=auction.lot)

        return render(request, self.template_name, context={
            "category": category,
            "auctionform": a,
            "productform": p,
            "auction": auction,

        })

    def post(self, request, *args, **kwargs):
        id = kwargs['id']
        category = Category.objects.filter(owner=None)
        auction = Auction.objects.get(pk=id)
        a = AuctionForm(instance=auction, data=request.POST)
        p = ProductForm(instance=auction.lot, data=request.POST, files=request.FILES)

        if a.is_valid() and p.is_valid():
            a.save()
            p.save()
            return redirect('profile')

        return render(request, self.template_name, context={
            "category": category,
            "auctionform": a,
            "productform": p,
            "auction": auction,

        })


class AuctionCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'auctioncore/auction_create.html'
    login_url = LOGIN_URL

    def get(self, request, *args, **kwargs):
        category = Category.objects.filter(owner=None)
        a = AuctionForm()
        p = ProductForm()

        return render(request, self.template_name, context={
            "category": category,
            "auctionform": a,
            "productform": p,

        })

    def post(self, request, *args, **kwargs):
        category = Category.objects.filter(owner=None)

        a = AuctionForm(data=request.POST)
        p = ProductForm(data=request.POST, files=request.FILES)

        images = dict(request.FILES)

        if a.is_valid() and p.is_valid():
            auction = a.save(commit=False)
            product = p.save(commit=False)
            auction.owner = request.user
            auction.save()
            product.auction = auction
            product.save()

            for i in images:
                ImageModel.objects.create(image=images[i][0], product=product)

            return redirect('profile')

        return render(request, self.template_name, context={
            "category": category,
            "auctionform": a,
            "productform": p,

        })


class AuctionDetailView(TemplateView):
    template_name = 'auctioncore/auction_detail.html'

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        category = Category.objects.filter(owner=None)
        auction = Auction.objects.get(pk=id)

        return render(request, self.template_name, context={
            "category": category,
            "auction": auction,

        })

    def post(self, request, *args, **kwargs):
        category = Category.objects.filter(owner=None)

        return render(request, self.template_name, context={
            "category": category,

        })


class AuctionMakeBetView(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        id = kwargs['id']
        d = dict(request.POST)
        auction = Auction.objects.get(id=id)
        bet = float(d['bet'][0].replace(',', '.'))
        Participants.objects.create(user=request.user, auction=auction, bet=bet)

        return redirect('auction_detail', id=id)


class AuctionCommentView(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        id = kwargs['id']
        auction = Auction.objects.get(id=id)
        d = dict(request.POST)
        comment = d['comment'][0]
        try:
            star = int(d['rating'][0])
        except:
            star = 0
        Acomments.objects.create(comment=comment, star=star, user=request.user, auction=auction)
        s = 0

        for c in auction.comments.all():
            s += c.star
        s = round(s / auction.comments.all().count())
        auction.star = s
        auction.save()
        return redirect('auction_detail', id=id)
