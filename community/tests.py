from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User, Group 
# Create your tests here.

from .models import Profile, Discipline, ResearchField, ResearchEstablishment

class CommunityTestCase(APITestCase):
    
    def test_create_and_update_profile(self):
        """
        Test profile creation
        """
        url = reverse('create-user-profile')
        data = {"username": "TestUsername","password": "testPassword","email" : "test@email.com"}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(User.objects.count(), 1)
        id = str(User.objects.get().id)
        print(id)
        # url = reverse('update-user-profile')
        data = {"username": "ModifiedTestUsername","email" : "testmodified@email.com"}
        response = self.client.put('update/1/', data, format='json')
        print(response)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get().username, "ModifiedTestUsername")
    
    def test_create_discipline(self):
        """
        Test discipline creation
        """

        url = reverse('create-discipline')
        data = {"user": 1,"discipline": "Test discipline","commentsDiscipline": "Test comment discipline"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Discipline.objects.count(), 1)
        self.assertEqual(Discipline.objects.get().discipline, 'Test discipline')
    
    def test_create_research_field(self):
        """
        Test research field creation
        """

        url = reverse('create-research-field')
        data = {"user": 1,"researchField": "Test research field","commentsResearch": "Test comment research"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ResearchField.objects.count(), 1)
        self.assertEqual(ResearchField.objects.get().researchField, 'Test research field')

    def test_create_research_establishment(self):
        """
        Test research establishment creation
        """

        url = reverse('create-research-establishment')
        data = {"user": 1,"laboratory": "Test laboratory","establishment": "Test establishment","commentsResearch": "Testcommentestablishment"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ResearchEstablishment.objects.count(), 1)
        self.assertEqual(ResearchEstablishment.objects.get().laboratory, 'Test laboratory')
    
    
