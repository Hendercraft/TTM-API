from rest_framework import viewsets, status
from django.contrib.auth.models import User, Group
from rest_framework.decorators import action
from rest_framework.response import Response
# from rest_framework import request
from community.serializers import UserSerializer, GroupSerializer, DisciplineSerializer, ResearchEstablishmentSerializer, ResearchFieldSerializer
from community.utils import create_user_account
from . import serializers

from community.models import Discipline, ResearchEstablishment, ResearchField
from API import accessPolicy

from django.shortcuts import get_object_or_404

"""
Users & groups
"""
class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [accessPolicy.UsersPolicy, ]

    @property
    def access_policy(self):
        return self.permission_classes[0]
    
    # def get_queryset(self):
    #     return self.access_policy.scope_queryset(
    #         self.request.data, User.objects.all()
    #     )

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
    
    # def get_queryset(self):
    #     return self.access_policy.scope_queryset(
    #         self.request, Group.objects.all()
    #     )

class DisciplineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow discipline model to be viewed or edited
    """
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [accessPolicy.DisciplinePolicy]

    # def retrieve(self, request, pk=None):
    #     queryset = Discipline.objects.all()
    #     Discipline = get_object_or_404(queryset, pk=pk)
    #     serializer = DisciplineSerializer(Discipline)
    #     return Response(serializer.data)

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