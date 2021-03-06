import decimal

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Auction, Participants, Acomments, Favorite
from django.contrib.auth.mixins import LoginRequiredMixin
from category.models import Category, SubCategory
from auction.settings import LOGIN_URL
from .forms import AuctionForm
from product.forms import ProductForm
from product.models import ImageModel
import operator
from .tools import is_time_out


class AuctionDeleteView(LoginRequiredMixin, TemplateView):
    login_url = LOGIN_URL

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        a = Auction.objects.get(pk=id)
        if request.user == a.owner:
            a.delete()

        return redirect('profile')


class ParticipantsDeleteView(LoginRequiredMixin, TemplateView):
    login_url = LOGIN_URL

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        a = Auction.objects.get(pk=id)
        u = request.user
        p = Participants.objects.get(auction=a, user=u)
        if p.bet == a.last_bet:
            p.delete()
            p = Participants.objects.filter(auction=a)[0]
            if p:
                a.last_bet = p.bet
            else:
                a.last_bet = a.start_price
            a.next_bet = a.last_bet + decimal.Decimal(a.start_price / 100 * a.increment)
            a.save()
        else:
            p.delete()

        return redirect('profile')


class AuctionEditView(LoginRequiredMixin, TemplateView):
    template_name = 'auctioncore/auction_edit.html'
    login_url = LOGIN_URL

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        category = Category.objects.all().order_by('order')

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
        category = Category.objects.all().order_by('order')

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
        category = Category.objects.all().order_by('order')

        a = AuctionForm()
        p = ProductForm()

        return render(request, self.template_name, context={
            "category": category,
            "auctionform": a,
            "productform": p,

        })

    def post(self, request, *args, **kwargs):
        category = Category.objects.all().order_by('order')

        a = AuctionForm(data=request.POST)
        p = ProductForm(data=request.POST, files=request.FILES)

        images = dict(request.FILES)

        if a.is_valid() and p.is_valid():
            auction = a.save(commit=False)
            product = p.save(commit=False)
            auction.owner = request.user
            auction.last_bet = auction.start_price
            auction.next_bet = auction.last_bet + decimal.Decimal(auction.start_price / 100 * auction.increment)

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
        category = Category.objects.all().order_by('order')

        auction = Auction.objects.get(pk=id)

        return render(request, self.template_name, context={
            "category": category,
            "auction": auction,

        })

    def post(self, request, *args, **kwargs):
        category = Category.objects.all().order_by('order')

        return render(request, self.template_name, context={
            "category": category,

        })


class AuctionsView(TemplateView):
    template_name = 'auctioncore/auctions.html'

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        type = kwargs['type']
        is_time_out()
        category = Category.objects.all().order_by('order')
        a = []
        if type == '1':
            if id == '0':
                a = Auction.objects.all()
            else:
                a = Auction.objects.filter(category_id=id)
        elif type == '2':
            sc = SubCategory.objects.get(pk=id)

            a = Auction.objects.filter(subcategory=sc, category=sc.owner)
        elif type == '3':
            a = Auction.objects.filter(category_id=id)
        search = ''
        try:
            search = request.GET.get('search')
        except:
            pass
        if search:
            a = a.filter(Q(title__icontains=search))

        return render(request, self.template_name, context={
            "category": category,
            "auctions": a,
            "type": type,
            "id": id,

        })

    def post(self, request, *args, **kwargs):
        category = Category.objects.all().order_by('order')

        return render(request, self.template_name, context={
            "category": category,

        })


class AuctionMakeBetView(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        id = kwargs['id']
        d = dict(request.POST)

        auction = Auction.objects.get(id=id)
        if request.user == auction.owner:
            return redirect('auction_detail', id=id)
        puser = Participants.objects.filter(auction=auction, user=request.user)

        if puser:
            if puser.first().bet == auction.last_bet:
                return redirect('auction_detail', id=id)
            else:
                puser.delete()
        bet = float(d['bet'][0].replace(',', '.'))
        Participants.objects.create(user=request.user, auction=auction, bet=bet)
        auction.last_bet = decimal.Decimal(bet)
        auction.next_bet = auction.last_bet + decimal.Decimal(auction.start_price / 100 * auction.increment)
        auction.save()
        return redirect('auction_detail', id=id)


def auctionFavorite(request):
    id = request.GET.get('id')
    user = request.user
    auction = Auction.objects.get(id=id)
    if user:
        if not Favorite.objects.filter(user=user, auction=auction):
            Favorite.objects.create(user=user, auction=auction)
    return HttpResponse(request, 'success')


def deleteFavorite(request):
    id = request.GET.get('id')
    user = request.user
    auction = Auction.objects.get(id=id)
    Favorite.objects.get(user=user, auction=auction).delete()

    return HttpResponse(request, 'success')


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

        s = 0
        c = 0
        for i in Auction.objects.filter(owner=auction.owner):
            c += 1
            if i.star:
                s += i.star
        s /= c
        s = s * 100 / 5

        s = round(s / c)
        auction.owner.profile.star = s
        auction.owner.profile.save()

        return redirect('auction_detail', id=id)


def loadSubCategories(request):
    category_id = request.GET.get('category')
    sc = SubCategory.objects.filter(owner_id=category_id).order_by('order')

    return render(request, 'auctioncore/ajax_loadSubCat.html', {'sc': sc})


def loadAuctionsBy(request):
    is_time_out()
    type = request.GET.get('type')

    id = request.GET.get('id')
    by = request.GET.get('by')
    ss = request.GET.get('ss')

    order = ['created_date', 'start_price', 'star', 'title'][int(by)]
    if ss == '2':
        order = '-' + order

    a = []
    if type == '1':
        if id == '0':
            a = Auction.objects.all().order_by(order)
        else:
            a = Auction.objects.filter(category_id=id).order_by(order)
    elif type == '2':
        sc = SubCategory.objects.get(pk=id).order_by(order)

        a = Auction.objects.filter(subcategory=sc, category=sc.owner).order_by(order)
    elif type == '3':
        a = Auction.objects.filter(category_id=id).order_by(order)

    return render(request, 'auctioncore/ajax_loadAuctions.html', {'auctions': a})
