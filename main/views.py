from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from category.models import Category


class MainView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        # Category
        category = Category.objects.filter(owner=None)
        for i in category:
            print(i.title)
            if i.subcategories:
                print(i.subcategories.all())
                for j in i.subcategories.all():
                    print("*" + j.title)

        return render(request, self.template_name, context={
            "category": category,
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })
