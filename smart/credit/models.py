from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class  DemandeDePret(models.Model):
    Numtelephone = models.DecimalField(max_digits=8, decimal_places=0, unique=True)
    num_compte = models.CharField(max_length=20)
    duree_emprunt = models.IntegerField()
    montant_emprunt = models.DecimalField(max_digits=10, decimal_places=2)
    cni = models.FileField(upload_to='cni/')
    demande = models.FileField(upload_to='demande/')
    contrat_de_travail = models.FileField(upload_to='contrats_de_travail/')
    attestation_travail = models.FileField(upload_to='attestations_travail/')
    justification_adresse = models.FileField(upload_to='justifications_adresse/')
    bulletins_de_salaire = models.FileField(upload_to='bulletins_de_salaire/')

class Bank(models.Model):
    name = models.CharField(max_length=250)
    adresse = models.CharField(max_length=250)
    email= models.CharField(max_length=250)



class Client(models.Model):
    name = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    adresse = models.CharField(max_length=250)
    NNI = models.DecimalField(max_digits=10, decimal_places=0, unique=True, primary_key=True)
    Numtelephone = models.DecimalField(max_digits=8, decimal_places=0, unique=True)


class Account(models.Model):
    """Represents Bank Account"""
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    open_date = models.CharField(max_length=250)
    account_type = models.CharField(max_length=250)
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE)    


class Withdraw(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)


class Deposit(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)