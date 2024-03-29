from django.contrib.auth.models import User, Group
from django.contrib.auth import password_validation
from django.contrib.auth.models import BaseUserManager
from django.core.mail import send_mail
from django.db.models import fields
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
        model = UserProfile
        exclude = ['password']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','username','password','first_name','last_name','email']

    def create(self, validated_data):
        password = validated_data.pop('password') # As a result password can be set proprely (hash)
        user = UserProfile.objects.create_user(**validated_data)
        user.groups.set(Group.objects.filter(name='publicUser')) #For new users -> automaticaly publicUsers
        user.set_password(password)
        user.save()
        return user

class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimony
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



#Contact messages

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
    
    def create(self, validated_data):

        contactMessage = Contact.objects.create(**validated_data)
        contactMessage.save()
        
        send_mail(contactMessage.subject, contactMessage.message, contactMessage.email, ['gabriel.garcia@utbm.fr'])

        return contactMessage


# class ProfileSerializer(serializers.ModelSerializer):
#     user = UserSerializer(many=False,required=False)  # May be an anonymous user.

#     #If the user is a researcher
#     discipline = DisciplineSerializer(required=False)
#     researchField = ResearchFieldSerializer(required=False)
#     researchEstablishment = ResearchEstablishmentSerializer(required=False)
    
#     class Meta:
#         model = Profile
#         fields = ['id','user','postalAdress','phoneNumber','profileImage','workedOnTheSite','workedInCompany','workTimeDuration','discipline','researchField','researchEstablishment']
      
#     def update(self, instance, validated_data):
#         user_data = validated_data.pop('user')
#         user = instance.user
#         instance.postalAdress = validated_data.get('postalAdress', instance.postalAdress)
#         instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
#         instance.profileImage = validated_data.get('profileImage', instance.profileImage)
#         instance.workedOnTheSite = validated_data.get('workedOnTheSite', instance.workedOnTheSite)
#         instance.workedInCompany = validated_data.get('workedInCompany', instance.workedInCompany)
#         instance.workTimeDuration = validated_data.get('workTimeDuration', instance.workTimeDuration)
#         instance.save()
    
#         user.username = user_data.get(
#             'username',
#             user.username
#         )
#         user.first_name = user_data.get(
#             'first_name',
#             user.first_name
#         )
#         user.last_name = user_data.get(
#             'last_name',
#             user.last_name
#         )
#         user.email = user_data.get(
#             'email',
#             user.email
#         )
#         user.save()
#         return instance

#     def delete(self,instance):
#         instance.user.is_active = False
#         return instance