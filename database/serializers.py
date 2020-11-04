from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import *


"""
Users & groups
"""



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

"""
Database
"""

#DATE
class DateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Date
        fields = ['name', 'date', 'duration_date']


#Quality
class QualitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quality
        fields = ['name', 'definition']


#Source & associates
class SourceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SourceType
        fields = ['typesSource']

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'lastName', 'status', 'organisation']

class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
        fields = ['sourceContent']

class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Url
        fields = ['url']

class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Source
       fields = ['name','author','date','types','content','url','viability','conservationPlace','cote']

# Place & associates
class PlaceLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlaceLocation
        fields = ['street_number', 'street_type', 'street_name', 'city', 'post_code', 'country', 'said_place']

class PlaceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlaceType
        fields = ['placeType']

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ['name', 'description', 'place_location', 'longitude', 'latitude', 'place_type', 'source']

#Knowledge
class KnowledgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Knowledge
        fields = ['name', 'definition']

#Collective Actor
class CollectiveActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CollectiveActor
        fields = ['name', 'definition', 'date', 'quality', 'knowledge', 'place', 'source']

#Abstract object
class AbstractOvjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbstractObject
        fields = ['name', 'definition', 'date', 'quality', 'collectiveActor', 'place', 'source']

#Profession
class ProfessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profession
        fields = ['name', 'definition', 'autonomous', 'abstractObject', 'place', 'source']

#Social activities
class SocialActivitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SocialActivity
        fields = ['name', 'definition', 'place', 'source']

#Social link
class SocialLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SocialLink
        fields = ['link', 'actorlink']

#Actor & associates
class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ['gender', 'profession', 'socialActivities', 'collectiveActors', 'quality', 'socialLink', 'place', 'source']

class NameActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NameActor
        fields = ['actors', 'name', 'last_name', 'typeOfActor']

#Object & associates
class DetailCaracteristicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetailCaracteristic
        fields = ['detailCaracteristicsObject']

class TypeObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeObject
        fields = ['typeObject']

class EnergySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Energy
        fields = ['energy']

class ObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Object
        fields = ['name', 'definition', 'brand', 'content', 'date', 'type_object', 'collectiveActors', 'actor', 'abstract_object', 'energy', 'place', 'source']

class CaracteristicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Caracteristic
        fields = ['objectCaracteristic', 'length', 'width', 'height', 'weight', 'surface', 'detail_caracteristics', 'source']
