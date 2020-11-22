from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from database.serializers import UserSerializer, GroupSerializer, DateSerializer, QualitySerializer, SourceTypeSerializer, AuthorSerializer, ContentSerializer, UrlSerializer, SourceSerializer
from database.models import Date, Quality, SourceType, Author, Content, Url, Source

# Create your views here.

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


"""
Users & groups
"""
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def create(self,request):
    #     pass
    # def update(self,request):
    #     pass


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

"""
Database
"""

class DateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Dates to be edited or viewed
    """
    queryset = Date.objects.all().order_by('-date')
    serializer_class = DateSerializer

class QualityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Qualities to be edited or viewed
    """
    queryset = Quality.objects.all().order_by('name')
    serializer_class = QualitySerializer


class SourceTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows source types to be edited or viewed
    """
    queryset = SourceType.objects.all()
    serializer_class = SourceTypeSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be edited or viewed
    """
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer

class ContentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contents to be edited or viewed
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class UrlViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows urls to be edited or viewed
    """
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

class SourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sources to be edited or viewed
    """
    queryset = Source.objects.all().order_by('-date')
    serializer_class = SourceSerializer
    #return Response(serializer.data)
