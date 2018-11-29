# DJANGO IMPORTS
from django.shortcuts import render
from django.views.generic import TemplateView
from rewind.forms import SignUpForm, SignUp2Form
from django.contrib.auth import login, authenticate
from .models import Utente

# View for the Homepage

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'home.html', context=None)

# View for the page chi siamo

class ChiSiamoView(TemplateView):
    template_name = "Chi_Siamo.html"

# View for the page FAQ

class FAQView(TemplateView):
    template_name = "FAQ.html"

# View for the Log In System

class AuthenticationView(TemplateView):
    template_name = "login.html"

# View for the Sing Up system

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form2 = SignUp2Form(request.POST)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            username = form.cleaned_data.get('username')
            user = Utente.objects.get(username=username)
            raw_password = form.cleaned_data.get('password')
            user.set_password(raw_password)
            user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
    else:
        form = SignUpForm()
        form2 = SignUp2Form()
    return render(request, 'registration/signup.html', {'form': form, 'form2': form2})

