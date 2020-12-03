from django.contrib.auth.models import User, Group
from django.contrib.auth import password_validation
from django.contrib.auth.models import BaseUserManager
from rest_framework import serializers
from community.models import *


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password','first_name','last_name', 'email', 'last_login', 'date_joined', 'groups', 'is_active', 'is_staff']
        # fields = '__all__'
    
    

    # def validate_password(self, value):
    #     password_validation.validate_password(value)
    #     return value
    
    # def get_auth_token(self, obj):
    #     token = Token.objects.create(user=obj)
    #     return token.key


class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'
    
    # def get_fields(self, *args, **kwargs):
    #     fields = super().get_fields(*args, **kwargs)
    #     request = self.context.get('request')
    #     if request is not None and not request.parser_context.get('kwargs'):
    #         fields.pop('password', None)
    #     return fields
    
    def create(self, validated_data):
        print(validated_data)
        user_data = validated_data.pop('user')
        print(user_data)
        password = validated_data.pop('password') # As a result password can be set proprely (hash)
        try:
            groups = validated_data.pop('groups') # Because many to many relationship
        except:
            print("You didn't send wich group the user is related")

        user = User.objects.create(**user_data)
        user.groups.set(groups)
        user.set_password(password)
        user.save()
        profile = Profile.objects.create(user=user,**validated_data)
        profile.save()
        return profile

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'


    def create(self, validated_data):
        print(validated_data)
        discipline = Discipline.objects.create(**validated_data)
        discipline.save()
        return discipline

class ResearchFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchField
        fields = '__all__'

class ResearchEstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchEstablishment
        fields = '__all__'