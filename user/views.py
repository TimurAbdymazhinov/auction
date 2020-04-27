from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm

from category.models import Category


class Login(TemplateView):
    template_name = 'user/logreg/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })


class RegistrationView(TemplateView):
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()

        return render(request, self.template_name, context={
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(data=request.POST)
        print(form.errors)
        if form.is_valid():

            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            return redirect('index')
        return render(request, self.template_name, context={
            'form': form
        })


class ProfileView(TemplateView):
    template_name = 'user/profile.html'

    def get(self, request, *args, **kwargs):
        category = Category.objects.filter(owner=None)

        return render(request, self.template_name, context={
            "category": category,
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })
