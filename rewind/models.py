from django.db import models
from django.contrib.auth.models import User

# Modello che estende il modello dell'utente

# class User(AbstractUser):
#     codice_utente = models.CharField(max_length=30, blank=False, unique=True)
#     citta = models.CharField(max_length=30, blank=True)
#     cap = models.IntegerField(null=True, blank=True)
#     via = models.CharField(max_length=30, blank=True)
#     Tipologia_Choices = (
#         ('', '-----------------'),
#         ('mono', 'monolocale'),
#         ('bil', 'bilocale'),
#         ('tri', 'trilocale/appartamento'),
#         ('abind', 'abitazione indipendente'),
#     )
#     tipologia = models.TextField(max_length=100, choices=Tipologia_Choices, default='', blank=True)
#     n_componenti = models.IntegerField(default=1)
#     punti = models.IntegerField(default=0)
#
# # Modello che contiene tutte le transazioni fatte dagli utenti
#
# class CronologiaPunti(models.Model):
#     utente = models.ForeignKey(User, on_delete=models.CASCADE)
#     punti_spesi = models.IntegerField()
#     transazione = models.CharField(max_length=50)
#
#
# # Modello che contiene i codici di registrazione degli utenti
#
# class CodiciRegistrazione(models.Model):
#     codice = models.CharField(max_length=30, blank=True)
