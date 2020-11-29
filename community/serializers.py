from django.contrib.auth.models import User, Group
from django.contrib.auth import password_validation
from django.contrib.auth.models import BaseUserManager
from rest_framework import serializers
from community.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name', 'email', 'last_login', 'date_joined', 'groups', 'is_active', 'is_staff']
        # fields = '__all__'
    
    def create(self, validated_data):
        print(validated_data)
        password = validated_data.pop('password') # As a result password can be set proprely (hash)
        groups = validated_data.pop('groups') # Because many to many relationship
        user_permissions = validated_data.pop('user_permissions') # Because many to many relationship
        user = User.objects.create(**validated_data)
        user.groups.set(groups)
        user.user_permissions.set(user_permissions)
        user.set_password(password)
        user.save()
        return user

    # def validate_password(self, value):
    #     password_validation.validate_password(value)
    #     return value
    
    # def get_auth_token(self, obj):
    #     token = Token.objects.create(user=obj)
    #     return token.key

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class Profile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'

class ResearchFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchField
        fields = '__all__'

class ResearchEstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchEstablishment
        fields = '__all__'