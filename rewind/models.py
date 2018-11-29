from django.db import models


class Utente(models.Model):

    codiceU = models.CharField(max_length=30, blank=False, unique=True)
    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=30, blank=False)
    punti = models.IntegerField(default=0)


class CronologiaPunti(models.Model):

    codice = models.ForeignKey(Utente, on_delete=models.CASCADE)
    transazione = models.CharField(max_length=50)


class Azienda(models.Model):

    codiceA = models.CharField(max_length=30, blank=True, unique=True)
    password = models.CharField(max_length=30, blank=True)
    nome = models.CharField(max_length=30, blank=True)
    ragionesociale = models.CharField(max_length=30, blank=True)
