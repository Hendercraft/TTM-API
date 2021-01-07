from rest_framework import serializers
from .models import *


"""
Database
"""

#DATE
class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = '__all__'


#Quality
class QualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quality
        fields = '__all__'


#Source & associates
class SourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceType
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
       model = Source
       fields = '__all__'

# Place & associates
class PlaceLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceLocation
        fields = '__all__'

class PlaceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceType
        fields = '__all__'

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

#Knowledge
class KnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Knowledge
        fields = '__all__'

#Collective Actor
class CollectiveActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectiveActor
        fields = '__all__'

#Abstract object
class AbstractOvjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractObject
        fields = '__all__'

#Profession
class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'

#Social activities
class SocialActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialActivity
        fields = '__all__'

#Social link
class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'

#Actor & associates
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class NameActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameActor
        fields = '__all__'

#Object & associates
class DetailCaracteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailCaracteristic
        fields = '__all__'

class TypeObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeObject
        fields = '__all__'

class EnergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Energy
        fields = '__all__'

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = '__all__'

class CaracteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caracteristic
        fields = '__all__'

class ModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Modify
        fields = '__all__'