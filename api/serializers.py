from rest_framework import serializers
from kanban.models import Taches, Colonne

class TachesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Taches
        fields='__all__'
        
class ColonneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Colonne
        fields='__all__'
        
class createTachesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Taches
        fields=['titre_tache','ordre','id_colonne']     
