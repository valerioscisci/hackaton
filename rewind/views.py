# DJANGO IMPORTS
from django.shortcuts import render
from django.views.generic import TemplateView
from rewind.forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group

# View for the Homepage

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'home.html', context=None)

# View for the Log In System

class AuthenticationView(TemplateView):
    template_name = "login.html"

# View for the page Area Riservata

class AreaRiservataView(TemplateView):
    template_name = "Area_Riservata.html"


# View for the Sing Up system

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        #form2 = SignUp2Form(request.POST)
        if form.is_valid(): #and form2.is_valid():
            form.save()
            #form2.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            raw_password = form.cleaned_data.get('password')
            user.set_password(raw_password)
            user.save()
            user = authenticate(username=username, password=raw_password)
            my_group = Group.objects.get(name='Utenti')
            my_group.user_set.add(user)
            login(request, user)
    else:
        form = SignUpForm()
        #form2 = SignUp2Form()
    return render(request, 'registration/signup.html', {'form': form})

