from rest_framework import viewsets, status
from django.contrib.auth.models import User, Group
from rest_framework.decorators import action
from rest_framework.response import Response
# from rest_framework import request
from community.serializers import *
from community.utils import create_user_account
from . import serializers

from community.models import Profile, Discipline, ResearchEstablishment, ResearchField
from API import accessPolicy

from django.shortcuts import get_object_or_404


#Tests
from rest_framework import generics
from rest_framework.response import Response

from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import UserManager


"""
Users & groups
"""


class ListProfile(generics.ListAPIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CreateProfile(generics.CreateAPIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        username = request.user.username
        user = UserManager.create_user(username, email=None, password=None, **kwargs)
        return user

class ListUser(generics.ListAPIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

class RetrieveProfile(generics.RetrieveAPIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UpdateProfile(generics.UpdateAPIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer




class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # Profile.objects.order_by('id').values()
    # queryset = Profile.objects.values('id')
    # queryset = Profile.objects.all()
    # queryset = Profile.objects.values('id', 'user_id', 'phoneNumber', 'postalAdress', 'profileImage', 'discipline', 'researchEstablishment', 'researchEstablishment_id', 'researchField', 'researchField_id', 'workTimeDuration', 'workedInCompany', 'workedOnTheSite')
    serializer_class = ProfileSerializer
    permission_classes = [accessPolicy.ProfilePolicy, ]

    # def get(self, request):
    #    queryset = Person.objects.all()
    #    serializer_class = PersonListSerializer(queryset, many=True) #It may change the things
    #    return Response(serializer_class.data)

    @property
    def access_policy(self):
        return self.permission_classes[0]
    
    # def get_queryset(self):
    #     return self.access_policy.scope_queryset(
    #         self.request.data, User.objects.all()
    #     )

    def get_queryset(self):
        queryset = Profile.objects.values('id').filter('user')
        return queryset

    # @action(detail=True, methods=['put'])
    # def set_password(self, request, pk=None):
    #     user = self.get_object()
    #     serializer=UserSerializer(request.data)
    #     if serializer.is_valid():
    #         user.set_password(serializer.data['password'])
    #         user.save()
    #         return Response({'status': 'password set'})
    #     else:
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [accessPolicy.GroupPolicy]

    @property
    def access_policy(self):
        return self.permission_classes[0]
    
    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, Group.objects.all()
        )

class DisciplineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow discipline model to be viewed or edited
    """
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    # permission_classes = [accessPolicy.DisciplinePolicy, ]
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return serializer

    def perform_create(self, serializer):
        serializer.save()


    @property
    def access_policy(self):
        return self.permission_classes[0]
    
    # def get_queryset(self):
    #     return self.access_policy.scope_queryset(
    #         self.request, Discipline.objects.all()
    #     )


class ResearchFieldViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow research field model to be viewed or edited
    """
    queryset = ResearchField.objects.all()
    serializer_class = ResearchFieldSerializer
    permission_classes = [accessPolicy.ResearchFieldPolicy]

    @property
    def access_policy(self):
        return self.permission_classes[0]
    
    # def get_queryset(self):
    #     return self.access_policy.scope_queryset(
    #         self.request, ResearchField.objects.all()
    #     )

class ResearchEstablishmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow research establishment model to be viewed or edited
    """
    queryset = ResearchEstablishment.objects.all()
    serializer_class = ResearchEstablishmentSerializer
    permission_classes = [accessPolicy.ResearchEstablishmentPolicy]

    @property
    def access_policy(self):
        return self.permission_classes[0]
    
    # def get_queryset(self):
    #     return self.access_policy.scope_queryset(
    #         self.request, ResearchEstablishment.objects.all()
    #     )