from django.contrib.auth.models import User, Group
from django.contrib.auth import password_validation
from django.contrib.auth.models import BaseUserManager
from rest_framework.utils import model_meta
from rest_framework import serializers,request
from rest_framework.request import Request
from community.models import *

from django.http import request


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name', 'email', 'last_login', 'date_joined', 'groups', 'is_active', 'is_staff']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','first_name','last_name','email']

    def create(self, validated_data):
        password = validated_data.pop('password') # As a result password can be set proprely (hash)
        user = User.objects.create_user(**validated_data)
        user.groups.set(Group.objects.filter(name='publicUser')) #For new users -> automaticaly publicUsers
        user.set_password(password)
        user.save()
        profile = Profile(
            user=user
        )
        profile.save()
        return user

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'

    # def create(self, validated_data):
    #     print(validated_data)
    #     discipline = Discipline.objects.create(**validated_data)
    #     discipline.save()
    #     return discipline  


class ResearchFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchField
        fields = '__all__'

class ResearchEstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchEstablishment
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False,required=False)  # May be an anonymous user.

    #If the user is a researcher
    discipline = DisciplineSerializer(required=False)
    researchField = ResearchFieldSerializer(required=False)
    researchEstablishment = ResearchEstablishmentSerializer(required=False)
    
    class Meta:
        model = Profile
        fields = ['id','user','postalAdress','phoneNumber','profileImage','workedOnTheSite','workedInCompany','workTimeDuration','discipline','researchField','researchEstablishment']
    
    # id = serializers.PrimaryKeyRelatedField(read_only=True)
    # user = UserSerializer(required=False)  # May be an anonymous user.
    # postalAdress = serializers.CharField(required=False)
    # phoneNumber = serializers.IntegerField(required=False)
    # profileImage = serializers.URLField(required=False)
    

    # #If the user had worked on the site
    # workedOnTheSite = serializers.BooleanField(required=False)
    # workedInCompany = serializers.CharField(max_length=255, required=False)
    # workTimeDuration = serializers.IntegerField(required=False) # Number of years
    

    # #If the user is a researcher
    # discipline = DisciplineSerializer(required=False)
    # researchField = ResearchFieldSerializer(required=False)
    # researchEstablishment = ResearchEstablishmentSerializer(required=False)
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        instance.postalAdress = validated_data.get('postalAdress', instance.postalAdress)
        instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
        instance.profileImage = validated_data.get('profileImage', instance.profileImage)
        instance.workedOnTheSite = validated_data.get('workedOnTheSite', instance.workedOnTheSite)
        instance.workedInCompany = validated_data.get('workedInCompany', instance.workedInCompany)
        instance.workTimeDuration = validated_data.get('workTimeDuration', instance.workTimeDuration)
        instance.save()
    
        user.username = user_data.get(
            'username',
            user.username
        )
        user.first_name = user_data.get(
            'first_name',
            user.first_name
        )
        user.last_name = user_data.get(
            'last_name',
            user.last_name
        )
        user.email = user_data.get(
            'email',
            user.email
        )
        user.save()
        return instance

    def delete(self,instance):
        instance.user.is_active = False
        return instance