from rest_framework import serializers
from .models import *

class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Source
       fields = ('name','author','date','types','content','url','viability','conservationPlace','cote') 