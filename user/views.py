from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm

from auctioncore.tools import is_time_out
from category.models import Category
from auctioncore.models import Auction, Participants, Favorite
from auction.settings import LOGIN_URL
from .models import Profile
from .forms import UserForm, ProfileForm, MyAuthenticationForm, MyUserCreationForm
from django.contrib.auth.views import LoginView


class MyLoginView(LoginView):
    form_class = MyAuthenticationForm


class RegistrationView(TemplateView):
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = MyUserCreationForm()

        return render(request, self.template_name, context={
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            return redirect('index')
        print("yse")
        return render(request, self.template_name, context={
            'form': form
        })


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'

    login_url = LOGIN_URL

    def get(self, request, *args, **kwargs):
        is_time_out()
        category = Category.objects.all().order_by('order')
        n = [i for i in range(10)]

        auctions = Auction.objects.filter(owner=request.user).order_by('-created_date')
        parts = Participants.objects.filter(user=request.user).order_by('-bed_date')

        return render(request, self.template_name, context={
            "category": category,
            "n": n,
            "auctions": auctions,
            "part": parts

        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })


class ProfileSettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile_settings.html'

    login_url = LOGIN_URL

    def get(self, request, *args, **kwargs):
        category = Category.objects.all().order_by('order')

        u = UserForm(instance=request.user)
        p = ProfileForm(instance=request.user.profile)

        return render(request, self.template_name, context={
            "category": category,
            "userform": u,
            "profileform": p,

        })

    def post(self, request, *args, **kwargs):
        category = Category.objects.all().order_by('order')
        u = UserForm(instance=request.user, data=request.POST)
        p = ProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if u.is_valid() and p.is_valid():
            u.save()
            p.save()
            return redirect('profile')

        return render(request, self.template_name, context={
            "category": category,
            "userform": u,
            "profileform": p,

        })


class FavoriteView(TemplateView):
    template_name = 'user/favorite.html'

    def get(self, request, *args, **kwargs):
        category = Category.objects.all().order_by('order')
        fa = Favorite.objects.filter(user=request.user)
        return render(request, self.template_name, context={
            "category": category,
            "fa": fa,

        })

    def post(self, request, *args, **kwargs):
        category = Category.objects.all().order_by('order')

        return render(request, self.template_name, context={
            "category": category,

        })
