from rest_framework import serializers
from .models import  DemandeDePret
   



class DemandeDePretSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeDePret  
        fields = '__all__' 
       # ['Numtelephone', 'num_compte', 'duree_emprunt', 'montant_emprunt',
                 # 'cni', 'demande', 'contrat_de_travail',
                  #'attestation_travail', 'justification_adresse', 'bulletins_de_salaire']      
