from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from category.models import Category
from .models import Page


class AboutAuctionsView(TemplateView):
    template_name = 'banner/dPage.html'

    def get(self, request, *args, **kwargs):
        category = Category.objects.all().order_by('order')
        p = Page.objects.get(order=1)
        return render(request, self.template_name, context={
            "category": category,
            'page': p,

        })

    def post(self, request, *args, **kwargs):
        category = Category.objects.all().order_by('order')

        return render(request, self.template_name, context={
            "category": category,

        })


class ContactsView(TemplateView):
    template_name = 'banner/dPage.html'

    def get(self, request, *args, **kwargs):
        category = Category.objects.all().order_by('order')
        p = Page.objects.get(order=2)
        return render(request, self.template_name, context={
            "category": category,
            'page': p,

        })

    def post(self, request, *args, **kwargs):
        category = Category.objects.all().order_by('order')

        return render(request, self.template_name, context={
            "category": category,

        })


class AboutUsView(TemplateView):
    template_name = 'banner/dPage.html'

    def get(self, request, *args, **kwargs):
        category = Category.objects.all().order_by('order')
        p = Page.objects.get(order=3)
        return render(request, self.template_name, context={
            "category": category,
            'page': p,

        })

    def post(self, request, *args, **kwargs):
        category = Category.objects.all().order_by('order')

        return render(request, self.template_name, context={
            "category": category,

        })

