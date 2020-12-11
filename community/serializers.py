from django.contrib.auth.models import User, Group
from django.contrib.auth import password_validation
from django.contrib.auth.models import BaseUserManager
from rest_framework.utils import model_meta
from rest_framework import serializers
from community.models import *


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


class ProfileSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    user = UserSerializer(required=False)  # May be an anonymous user.
    postalAdress = serializers.CharField(required=False)
    phoneNumber = serializers.IntegerField(required=False)
    profileImage = serializers.URLField(required=False)
    

    #If the user had worked on the site
    workedOnTheSite = serializers.BooleanField(required=False)
    workedInCompany = serializers.CharField(max_length=255, required=False)
    workTimeDuration = serializers.IntegerField(required=False) # Number of years
    

    #If the user is a researcher
    discipline = DisciplineSerializer(required=False)
    researchField = ResearchFieldSerializer(required=False)
    researchEstablishment = ResearchEstablishmentSerializer(required=False)
    
    def update(self, instance, validated_data):
        # raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        # Simply set each attribute on the instance, and then save it.
        # Note that unlike `.create()` we don't need to treat many-to-many
        # relationships as being a special case. During updates we already
        # have an instance pk for the relationships to be associated with.
        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                setattr(instance, attr, value)

        instance.save()

        # Note that many-to-many fields are set after updating instance.
        # Setting m2m fields triggers signals which could potentially change
        # updated instance and we do not want it to collide with .update()
        for attr, value in m2m_fields:
            field = getattr(instance, attr)
            field.set(value)

        return instance

    def delete(self,user):
        user.is_active = False
        return user