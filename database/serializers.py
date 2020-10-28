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
        fields = ['type_source']

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'last_name', 'status', 'organisation']

class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
        fields = ['source_content']

class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Url
        field = ['url']

class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Source
       fields = ['name','author','date','types','content','url','viability','conservationPlace','cote'] 