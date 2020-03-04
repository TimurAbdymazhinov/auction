from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class Login(TemplateView):
    template_name = 'user/logreg/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })


class Registration(TemplateView):
    template_name = 'user/logreg/registration.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })
