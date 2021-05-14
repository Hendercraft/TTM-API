from community.pagination import *
from community.serializers import *
from community.models import *


from API.permission import *



from rest_framework import generics, mixins
from rest_framework.request import Request
from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny


#Profile
class CreateProfile(generics.CreateAPIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    queryset = UserProfile.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class ListProfile(generics.ListAPIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    queryset = UserProfile.objects.all().order_by('id')
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [AllowAny]


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve a user in the system.

    * Requires token authentication.
    * Only admin users and (is_user) are able to access this view.
    """

    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOrReadOnly]

class TestimonyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow testimony model to be viewed or edited
    """

    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser|IsAuthenticated|IsOwnerOrReadOnly]
        elif self.action == 'list':
            permission_classes = [IsOwnerOrReadOnly|IsAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsOwnerOrReadOnly|IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsOwnerOrReadOnly|IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DisciplineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow discipline model to be viewed or edited
    """

    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser|IsAuthenticated|IsOwnerOrReadOnly]
        elif self.action == 'list':
            permission_classes = [IsOwnerOrReadOnly|IsAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsOwnerOrReadOnly|IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsOwnerOrReadOnly|IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ResearchFieldViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow research field model to be viewed or edited
    """

    queryset = ResearchField.objects.all()
    serializer_class = ResearchFieldSerializer

    
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser|IsAuthenticated]
        elif self.action == 'list':
            permission_classes = [IsOwnerOrReadOnly|IsAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsOwnerOrReadOnly|IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsOwnerOrReadOnly|IsAdminUser]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ResearchEstablishmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow research establishment model to be viewed or edited
    """

    queryset = ResearchEstablishment.objects.all()
    serializer_class = ResearchEstablishmentSerializer


    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser|IsAuthenticated]
        elif self.action == 'list':
            permission_classes = [IsOwnerOrReadOnly|IsAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsOwnerOrReadOnly|IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsOwnerOrReadOnly|IsAdminUser]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
