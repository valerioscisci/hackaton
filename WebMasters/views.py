# DJANGO IMPORTS
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from WebMasters.forms import SingUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# View for the Homepage

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'home.html', context=None)

# View for the Log In System

class AuthenticationView(TemplateView):
    template_name = "login.html"

# View for the Sing Up system

def signup(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            raw_password = form.cleaned_data.get('password')
            user.set_password(raw_password)
            user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
    else:
        form = SingUpForm()
    return render(request, 'registration/signup.html', {'form': form})
