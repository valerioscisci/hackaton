from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email',)# 'codice_utente', 'citta', 'cap', 'via', 'tipologia','n_componenti','punti',)

        widgets = {
            'username': forms.TextInput(attrs={'class': 'required'}),
            'password': forms.PasswordInput(attrs={'class': 'required'}),
            'first_name': forms.TextInput(attrs={'class': 'notrequired'}),
            'last_name': forms.TextInput(attrs={'class': 'notrequired'}),
            'email': forms.EmailInput(attrs={'class': 'required'}),
            # 'codice_utente': forms.TextInput(attrs={'class': 'required'}),
            # 'citta': forms.TextInput(attrs={'class': 'notrequired'}),
            # 'cap': forms.NumberInput(attrs={'class': 'notrequired'}),
            # 'via': forms.TextInput(attrs={'class': 'notrequired'}),
            # 'tipologia': forms.Select(attrs={'class': 'notrequired'}),
            # 'n_componenti': forms.NumberInput(attrs={'class': 'notrequired'}),
        }