from rest_framework import serializers
from .models import *


"""
Database
"""


#Upload
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = "__all__"


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

#Knowledge
class KnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Knowledge
        fields = '__all__'

"""
Source & associates serializers
"""

#Source type
class SourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceType
        fields = '__all__'

#Author
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

#Content
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

#URl
class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'

#Source
class SourceSerializer(serializers.ModelSerializer):
    class Meta:
       model = Source
       fields = '__all__'

"""
Place & associates serializers
"""

# Place location
class PlaceLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceLocation
        fields = '__all__'

#Place type
class PlaceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceType
        fields = '__all__'

#PLace
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

"""
Collective actor serializer
"""

#Collective Actor
class CollectiveActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectiveActor
        fields = '__all__'

"""
Abstract object serializer
"""

#Abstract object
class AbstractObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractObject
        fields = '__all__'

#Profession
class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'

"""
Social activities & associates serializer
"""

#Social activity
class SocialActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialActivity
        fields = '__all__'

#Social link
class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'

"""
Actor & associates serializer
"""

#Actor
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

#Name actor
class NameActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameActor
        fields = '__all__'

"""
Object & associates serializer
"""

#Detail caracteristic
class DetailCaracteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailCaracteristic
        fields = '__all__'

#Type object
class TypeObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeObject
        fields = '__all__'

#Energy
class EnergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Energy
        fields = '__all__'

#Object
class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = '__all__'

#Caracteristic
class CaracteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caracteristic
        fields = '__all__'

#Modify
class ModifyAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModifyAttribute
        fields = '__all__'