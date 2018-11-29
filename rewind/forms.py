from django import forms
from .models import Utente

class SingUpForm(forms.ModelForm):
    class Meta:
        model = Utente
        fields = ('codiceU', 'username', 'password',)

        widgets = {

            'codiceU': forms.TextInput(attrs={'class': 'required'}),
            'username': forms.TextInput(attrs={'class': 'required'}),
            'password': forms.PasswordInput(attrs={'class': 'required'}),
        }
