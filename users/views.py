from rest_framework import viewsets, permissions, status
from django.contrib.auth.models import User, Group
from rest_framework.decorators import action
from rest_framework.response import Response
from users.serializers import UserSerializer, GroupSerializer
from users.utils import create_user_account
from . import serializers

# Create your views here.
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

    # @action(detail=True, methods=['post'])
    # def reset_password(self, request, pk=None):
    #     user = self.get_object()
    #     serializer = PasswordSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user.set_password(serializer.data['password'])
    #         user.save()
    #         return Response({'status': 'password set'})
    #     else:
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)

    # def create(self, request, *args, **kwargs):

    #     try:
    #         User.objects.create_user(request, *args, **kwargs)
    #     except:
    #         return Response({'status': 'Error during creation'})
    #     return Response({'status': 'User created successfully'})


    # def update(self,request):
    #     pass

    # @action(methods=['POST', ], detail=False)
    # def register(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = create_user_account(**serializer.validated_data)
    #     data = serializers.UserSerializer(user).data
    #     return Response(data=data, status=status.HTTP_201_CREATED)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]