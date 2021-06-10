from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView

from django.contrib.postgres.search import SearchVector
from django.contrib.auth.models import Group
from database.serializers import *
from database.models import *

from API.permission import *
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

import json

@api_view(['POST'])
def Search(request):
    # Note the use of `get_queryset()` instead of `self.queryset`
    data = request.body
    query = json.loads(data)
    # queryset_date = Date.objects.filter(name__search=query["search"])
    queryset_date = Date.objects.annotate(search=SearchVector('name', 'date'),).filter(search=query["search"])
    queryset_quality = Quality.objects.filter(name__search=query["search"])
    # queryset_sourceType = SourceType.objects.filter(typeSource__search=query["search"])
    queryset_author = Author.objects.annotate(search=SearchVector('name', 'lastName'),).filter(search=query["search"])
    queryset_content = Content.objects.filter(sourceContent__search=query["search"])
    queryset_files = Files.objects.filter(name__search=query["search"])
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
    # serializer_sourceType = SourceTypeSerializer(queryset_sourceType, context={'request': request}, many=True)
    serializer_author = AuthorSerializer(queryset_author, context={'request': request}, many=True)
    serializer_content = ContentSerializer(queryset_content, context={'request': request}, many=True)
    serializer_files = FilesSerializer(queryset_files, context={'request': request}, many=True)
    serializer_source = SourceSerializer(queryset_source, context={'request': request}, many=True)
    serializer_placeLocation = PlaceLocationSerializer(queryset_placeLocation, context={'request': request}, many=True)
    serializer_placeType = PlaceTypeSerializer(queryset_placeType, context={'request': request}, many=True)
    serializer_place = PlaceSerializer(queryset_place, context={'request': request}, many=True)
    serializer_knowledge = KnowledgeSerializer(queryset_knowledge, context={'request': request}, many=True)
    serializer_collectiveActor = CollectiveActorSerializer(queryset_collectiveActor, context={'request': request}, many=True)
    serializer_abstractObject = AbstractObjectSerializer(queryset_abstractObject, context={'request': request}, many=True)
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
                        # serializer_sourceType.data,
                        serializer_author.data,
                        serializer_content.data,
                        serializer_files.data,
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
    queryset = ModifyAttribute.objects.all()
    serializer_class = ModifyAttributeSerializer
    permission_classes = [IsAdminUser|IsResearcherUser]

"""
Database 
"""

class DateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Dates to be edited or viewed
    """
    queryset = Date.objects.all().order_by('-date')
    serializer_class = DateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        data = self.request.data
        # object = self.get_context_data
        # id = object.objects.get().id
        print(object)
        # query = json.loads(data)
        for key, value in data.items():
            if key == 'id':
                self.id = value
            self.table = 'Date'
            self.attribute_value = key
            # self.instance_value = self.pk
            self.content = value
            ModifyAttribute.objects.create(table = self.table, field_value = self.attribute_value, instance_value = 1, content = self.content) 
        serializer.save(validated=False)


class QualityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Qualities to be edited or viewed
    """
    queryset = Quality.objects.all().order_by('name')
    serializer_class = QualitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class KnowledgeViewSet(viewsets.ModelViewSet):
    """
    API enpoint that allows knowledges to be edited or viewed
    """
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

"""
Sources & associates viewsets
"""

class RessourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows source types to be edited or viewed
    """
    queryset = Ressource.objects.all().order_by('id')
    serializer_class = RessourceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be edited or viewed
    """
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ContentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contents to be edited or viewed
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FilesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows urls to be edited or viewed
    """
    queryset = Files.objects.all()
    serializer_class = FilesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_form(self):
    #     if request.method == 'GET':

class SourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sources to be edited or viewed
    """
    queryset = Source.objects.all().order_by('date_source')
    serializer_class = SourceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

"""
Place & associates viewsets
"""

class PlaceLocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows place locations to be edited or viewed
    """
    queryset = PlaceLocation.objects.all()
    serializer_class = PlaceLocationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PlaceTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows place types to be edited or viewed
    """
    queryset = PlaceType.objects.all()
    serializer_class = PlaceTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows places to be edited or viewed
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

"""
Collective actor viewset
"""

class CollectiveActorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows collective actors to be edited or viewed
    """
    queryset = CollectiveActor.objects.all()
    serializer_class = CollectiveActorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

"""
Abstract object viewset
"""

class AbstractObjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abstract objects to be edited or viewed
    """
    queryset = AbstractObject.objects.all()
    serializer_class = AbstractObjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

"""
Profession viewset
"""

class ProfessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows professions to be edited or viewed
    """
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

"""
Social & associates viewsets
"""

class SocialActivityViewSet(viewsets.ModelViewSet):
    """
    API enpoint that allows social activities to be edited or viewed
    """
    queryset = SocialActivity.objects.all()
    serializer_class = SocialActivitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SocialLinkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows social links to be edited or viewed
    """
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

"""
Actor & associates viewsets
"""

class ActorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows actors to be edited or viewed
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class NameActorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows actors names to be edited or viewed
    """
    queryset = NameActor.objects.all()
    serializer_class = NameActorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

"""
Object & associates viewsets
"""

class DetailCaracteristicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows detail caracteristics of objects to be edited or viewed
    """
    queryset = DetailCaracteristic.objects.all()
    serializer_class = DetailCaracteristicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TypeObjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows type of objects to be edited or viewed
    """
    queryset = TypeObject.objects.all()
    serializer_class = TypeObjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EnergyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows energy of an object to be edited or viewed
    """
    queryset = Energy.objects.all()
    serializer_class = EnergySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TypologieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow building objects to be edited or viewed
    """
    queryset = Typologie.objects.all()
    serializer_class = TypologieSerializer
     

class ObjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows objects to be edited or viewed
    """
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CaracteristicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows caracteristics of an object to be edited or viewed
    """
    queryset = Caracteristic.objects.all()
    serializer_class = CaracteristicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
