from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# Create your views here.


class MainView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, context={
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })
