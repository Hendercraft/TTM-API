from rest_framework import viewsets, generics
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from django.contrib.postgres.search import SearchVector
from django.contrib.auth.models import Group
from database.serializers import *
from database.models import *

# Create your views here.

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

import json


@api_view(['POST'])
def Search(request):
    # Note the use of `get_queryset()` instead of `self.queryset`
    data = request.body
    query = json.loads(data)
    # queryset_date = Date.objects.filter(name__search=query["search"])
    queryset_date = Date.objects.annotate(search=SearchVector('name', 'date'),).filter(search=query["search"])
    queryset_quality = Quality.objects.filter(name__search=query["search"])
    queryset_sourceType = SourceType.objects.filter(typeSource__search=query["search"])
    queryset_author = Author.objects.annotate(search=SearchVector('name', 'lastName'),).filter(search=query["search"])
    queryset_content = Content.objects.filter(sourceContent__search=query["search"])
    queryset_url = Url.objects.filter(url__search=query["search"])
    queryset_source = Source.objects.annotate(search=SearchVector('name', 'date'),).filter(search=query["search"])
    queryset_placeLocation = PlaceLocation.objects.annotate(search=SearchVector('street_name', 'city'),).filter(search=query["search"])
    queryset_placeType = PlaceType.objects.filter(placeType__search=query["search"])
    queryset_place= Place.objects.filter(name__search=query["search"])
    queryset_knowledge = Knowledge.objects.filter(name__search=query["search"])
    queryset_collectiveActor = CollectiveActor.objects.filter(name__search=query["search"])
    queryset_abstractObject = AbstractObject.objects.filter(name__search=query["search"])
    queryset_profession = Profession.objects.filter(name__search=query["search"])
    queryset_socialActivity = SocialActivity.objects.filter(name__search=query["search"])
    queryset_socialLink = SocialLink.objects.filter(link__search=query["search"])
    queryset_nameActor = NameActor.objects.annotate(search=SearchVector('name', 'last_name'),).filter(search=query["search"])
    queryset_detailCaracteristic = DetailCaracteristic.objects.filter(detailCaracteristicsObject__search=query["search"])
    queryset_typeObject = TypeObject.objects.filter(typeObject__search=query["search"])
    queryset_energy = Energy.objects.filter(energy__search=query["search"])
    queryset_object = Object.objects.annotate(search=SearchVector('name', 'brand'),).filter(search=query["search"])
    queryset_caracteristic = Caracteristic.objects.annotate(search=SearchVector('length', 'surface'),).filter(search=query["search"])
    
    serializer_date = DateSerializer(queryset_date, context={'request': request}, many=True)
    serializer_quality = QualitySerializer(queryset_quality, context={'request': request}, many=True)
    serializer_sourceType = SourceTypeSerializer(queryset_sourceType, context={'request': request}, many=True)
    serializer_author = AuthorSerializer(queryset_author, context={'request': request}, many=True)
    serializer_content = ContentSerializer(queryset_content, context={'request': request}, many=True)
    serializer_url = UrlSerializer(queryset_url, context={'request': request}, many=True)
    serializer_source = SourceSerializer(queryset_source, context={'request': request}, many=True)
    serializer_placeLocation = PlaceLocationSerializer(queryset_placeLocation, context={'request': request}, many=True)
    serializer_placeType = PlaceTypeSerializer(queryset_placeType, context={'request': request}, many=True)
    serializer_place = PlaceSerializer(queryset_place, context={'request': request}, many=True)
    serializer_knowledge = KnowledgeSerializer(queryset_knowledge, context={'request': request}, many=True)
    serializer_collectiveActor = CollectiveActorSerializer(queryset_collectiveActor, context={'request': request}, many=True)
    serializer_abstractObject = AbstractOvjectSerializer(queryset_abstractObject, context={'request': request}, many=True)
    serializer_profession = ProfessionSerializer(queryset_profession, context={'request': request}, many=True)
    serializer_socialActivity = SocialActivitySerializer(queryset_socialActivity, context={'request': request}, many=True)
    serializer_socialLink = SocialLinkSerializer(queryset_socialLink, context={'request': request}, many=True)
    serializer_nameActor = NameActorSerializer(queryset_nameActor, context={'request': request}, many=True)
    serializer_detailCaracteristic = DetailCaracteristicSerializer(queryset_detailCaracteristic, context={'request': request}, many=True)
    serializer_typeObject = TypeObjectSerializer(queryset_typeObject, context={'request': request}, many=True)
    serializer_energy = EnergySerializer(queryset_energy, context={'request': request}, many=True)
    serializer_object = ObjectSerializer(queryset_object, context={'request': request}, many=True)
    serializer_caracteristic = CaracteristicSerializer(queryset_caracteristic, context={'request': request}, many=True)

    Serializer_list = [serializer_date.data, 
                        serializer_quality.data,
                        serializer_sourceType.data,
                        serializer_author.data,
                        serializer_content.data,
                        serializer_url.data,
                        serializer_source.data,
                        serializer_placeLocation.data,
                        serializer_placeType.data,
                        serializer_place.data,
                        serializer_knowledge.data,
                        serializer_collectiveActor.data,
                        serializer_abstractObject.data,
                        serializer_profession.data,
                        serializer_socialActivity.data,
                        serializer_socialLink.data,
                        serializer_nameActor.data,
                        serializer_detailCaracteristic.data,
                        serializer_typeObject.data,
                        serializer_energy.data,
                        serializer_object.data,
                        serializer_caracteristic.data,
                        ]
    
    return Response(Serializer_list)



class ModifyRessource(generics.ListAPIView):
    """
    API endpoint that allow reserchers to validate updated data
    """
    queryset = Modify.objects.all()
    serializer_class = ModifySerializer


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
