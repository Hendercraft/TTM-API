from rest_framework import viewsets, status
from django.contrib.auth.models import User, Group

from rest_framework.decorators import action
from rest_framework.permissions import BasePermission, AllowAny, SAFE_METHODS

from community.pagination import *
from community.serializers import *
from community.models import Profile, Discipline, ResearchEstablishment, ResearchField


from API import accessPolicy


#Tests
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework.permissions import IsAdminUser
import json


"""
Users & groups
"""

#Profile
class ListProfile(generics.ListAPIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer
    pagination_class = StandardResultsSetPagination

class CreateProfile(generics.CreateAPIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

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

class DeleteProfile(generics.RetrieveDestroyAPIView):
    """
    View to delete a user in the system.

    * Requires token authentication.
    * Only admin users or (is_user) are able to access this view.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = StandardResultsSetPagination
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
    pagination_class = StandardResultsSetPagination

    # permission_classes = [accessPolicy.DisciplinePolicy, ]

    # @property
    # def access_policy(self):
    #     return self.permission_classes[0]
    
    @action(detail=True, methods=['post'])
    def create(self, request, *args, **kwargs):
        data = request.body

        request_body = json.loads(data)

        if request.user.is_authenticated:
            discipline_obj = Discipline.objects.create(user=request.user, discipline=request_body["discipline"],commentsDiscipline=request_body["commentsDiscipline"])
            serializer = DisciplineSerializer(discipline_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
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
    pagination_class = StandardResultsSetPagination
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
    pagination_class = StandardResultsSetPagination
    # permission_classes = [accessPolicy.ResearchEstablishmentPolicy]

    @property
    def access_policy(self):
        return self.permission_classes[0]
    
    # def get_queryset(self):
    #     return self.access_policy.scope_queryset(
    #         self.request, ResearchEstablishment.objects.all()
    #     )
