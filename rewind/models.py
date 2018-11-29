from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Modello che estende il modello dell'utente

class Utente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    codice_utente = models.CharField(max_length=30, blank=False, unique=True)
    citta = models.CharField(max_length=30, blank=True)
    cap = models.IntegerField(blank=True)
    via = models.CharField(max_length=30, blank=True)
    Tipologia_Choices = (
        ('', '-----------------'),
        ('mono', 'monolocale'),
        ('bil', 'bilocale'),
        ('tri', 'trilocale/appartamento'),
        ('abind', 'abitazione indipendente'),
    )
    tipologia = models.TextField(max_length=100, choices=Tipologia_Choices, default='', blank=True)
    n_componenti = models.IntegerField(default=1)
    punti = models.IntegerField(default=0)

# Metodi per creare il profilo completo dell'utente

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Utente.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Modello che contiene tutte le transazioni fatte dagli utenti

class CronologiaPunti(models.Model):
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    punti_spesi = models.IntegerField()
    transazione = models.CharField(max_length=50)


# Modello che contiene i codici di registrazione degli utenti

class CodiciRegistrazione(models.Model):
    codice = models.CharField(max_length=30)
