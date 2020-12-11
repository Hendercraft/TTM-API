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
    serializer_class = RegisterSerializer


class RetrieveProfile(generics.RetrieveAPIView):
    """
    View to retrieve a user in the system.

    * Requires token authentication.
    * Only admin users and (is_user) are able to access this view.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UpdateProfile(generics.UpdateAPIView):
    """
    View to update a user in the system.

    * Requires token authentication.
    * Only admin users or (is_user) are able to access this view.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class DeleteProfile(generics.DestroyAPIView):
    """
    View to delete a user in the system.

    * Requires token authentication.
    * Only admin users or (is_user) are able to access this view.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    
    serializer_class = ProfileSerializer
    permission_classes = [accessPolicy.ProfilePolicy, ]


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
    # lookup_field = 'pk'


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
    # permission_classes = [accessPolicy.ResearchFieldPolicy]

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
    # permission_classes = [accessPolicy.ResearchEstablishmentPolicy]

    @property
    def access_policy(self):
        return self.permission_classes[0]
    
    # def get_queryset(self):
    #     return self.access_policy.scope_queryset(
    #         self.request, ResearchEstablishment.objects.all()
    #     )