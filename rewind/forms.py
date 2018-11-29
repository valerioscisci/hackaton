from django import forms
from django.contrib.auth.models import User

class SingUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email',)

        widgets = {
            'username': forms.TextInput(attrs={'class': 'required'}),
            'password': forms.PasswordInput(attrs={'class': 'required'}),
            'first_name': forms.TextInput(attrs={'class': 'notrequired'}),
            'last_name': forms.TextInput(attrs={'class': 'notrequired'}),
            'email': forms.EmailInput(attrs={'class': 'required'}),
        }
