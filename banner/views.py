from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from category.models import Category


class AboutAuctionsView(TemplateView):
    template_name = 'banner/aboutAuctions.html'

    def get(self, request, *args, **kwargs):

        category = Category.objects.all().order_by('order')

        return render(request, self.template_name, context={
            "category": category,

        })

    def post(self, request, *args, **kwargs):
        category = Category.objects.all().order_by('order')

        return render(request, self.template_name, context={
            "category": category,

        })


class ContactsView(TemplateView):
    template_name = 'banner/contacts.html'

    def get(self, request, *args, **kwargs):

        category = Category.objects.all().order_by('order')

        return render(request, self.template_name, context={
            "category": category,

        })

    def post(self, request, *args, **kwargs):
        category = Category.objects.all().order_by('order')

        return render(request, self.template_name, context={
            "category": category,

        })


class AboutUsView(TemplateView):
    template_name = 'banner/aboutUs.html'

    def get(self, request, *args, **kwargs):

        category = Category.objects.all().order_by('order')

        return render(request, self.template_name, context={
            "category": category,

        })

    def post(self, request, *args, **kwargs):
        category = Category.objects.all().order_by('order')

        return render(request, self.template_name, context={
            "category": category,

        })


class BlogView(TemplateView):
    template_name = 'banner/blog.html'

    def get(self, request, *args, **kwargs):

        category = Category.objects.all().order_by('order')

        return render(request, self.template_name, context={
            "category": category,

        })

    def post(self, request, *args, **kwargs):
        category = Category.objects.all().order_by('order')

        return render(request, self.template_name, context={
            "category": category,

        })
