from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, force_authenticate
from django.contrib.auth.models import User, Group 

from .models import Profile, Discipline, ResearchField, ResearchEstablishment

class CommunityTestCase(APITestCase):
    def setUp(self):
        #Create profile
        self.data = {"username": "TestUsername","password": "testPassword","email" : "test@email.com"}
        self.client.post(reverse('create-user-profile'), self.data, format='json')
        

        self.id = User.objects.get().id #get the id from user to update data

        print("User "+str(self.id)+" created with name "+User.objects.get().username)
        
        #With JWT
        # self.data = {"username": "TestUsername","password": "testPassword"}
        # response = self.client.post(reverse('token_obtain_pair'), self.data, format='json')
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['access'])
        # print(self.client.head(reverse('token_obtain_pair'), self.data))
        # print(self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['access']))
        # print(self.client.login)
        
        # print(self.assertTrue(
        # print(User.objects.get().password)
        # print(self.id)
    
    def test_update_retrieve_delete_profile(self):
        """
        Test profile create_update_retrieve_delete
        """
        #create profile
        self.data = {
            "user":
            {
                "username": "ModifiedTestUsername","email" : "testmodified@email.com"
            }
            }
        response = self.client.put(reverse('update-user-profile', args=(self.id,)), self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get().username, "ModifiedTestUsername")

        #Retrieve profile
        response = self.client.get(reverse('retrieve-user-profile', args=(self.id,)))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #delete profile
        response = self.client.delete(reverse('delete-user-profile',args=(self.id,)))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_create_update_retrieve_delete_discipline(self):
        """
        Test discipline create_update_retrieve_delete
        """        
        #Create discipline
        
        user = User.objects.get(username='TestUsername')
        self.client.force_authenticate(user=user)

        # self.client.login(username='TestUsername',password='testPassword')

        self.data = {"user": self.id, "discipline": "Test discipline","commentsDiscipline": "Test comment discipline"}
        response = self.client.post(reverse('create-discipline'), self.data, format='json')

        self.assertEqual(response.content.decode(), '201')
        self.assertEqual(Discipline.objects.count(), 1)
        self.assertEqual(Discipline.objects.get().discipline, 'Test discipline')
        self.id = Discipline.objects.get().id

        #Retrieve discipline
        response = self.client.get(reverse('retrieve-discipline', args=(self.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #update discipline
        self.data = {"discipline": "ModifiedDiscipline","commentsDiscipline" : "Modified Comment discipline"}
        response = self.client.put(reverse('update-discipline', args=(self.id,)), self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Discipline.objects.get().discipline, "ModifiedDiscipline")
        self.assertEqual(Discipline.objects.get().commentsDiscipline, "Modified Comment discipline")

        #delete discipline
        response = self.client.delete(reverse('delete-discipline',args=(self.id,)))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_create_update_retrieve_delete_research_field(self):
        """
        Test research field create_update_retrieve_delete
        """
        #Create research field
        self.data = {"user": self.id,"researchField": "Test research field","commentsResearch": "Test comment research"}
        response = self.client.post(reverse('create-research-field'), self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ResearchField.objects.count(), 1)
        self.assertEqual(ResearchField.objects.get().researchField, 'Test research field')
        self.id = ResearchField.objects.get().id

        #Retrieve research field
        response = self.client.get(reverse('retrieve-research-field', args=(self.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #update research field
        self.data = {"researchField": "Modified research field","commentsResearch" : "Modified comment research"}
        response = self.client.put(reverse('update-research-field', args=(self.id,)), self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ResearchField.objects.get().researchField, "Modified research field")
        self.assertEqual(ResearchField.objects.get().commentsResearch, "Modified comment research")

        #delete research field
        response = self.client.delete(reverse('delete-research-field',args=(self.id,)))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_update_retrieve_delete_research_establishment(self):
        """
        Test research establishment create_update_retrieve_delete
        """
        #Create research establishment
        self.data = {"user": self.id,"laboratory": "Test laboratory","establishment": "Test establishment","commentsEstablishment": "Test comment establishment"}
        response = self.client.post(reverse('create-research-establishment'), self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ResearchEstablishment.objects.count(), 1)
        self.assertEqual(ResearchEstablishment.objects.get().laboratory, 'Test laboratory')
        self.id = ResearchEstablishment.objects.get().id

        #Retrieve research establishment
        response = self.client.get(reverse('retrieve-research-establishment', args=(self.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #update research establishment
        self.data = {"laboratory": "Modified laboratory","establishment" : "Modified establishment", "commentsEstablishment": "Modified comment establishment"}
        response = self.client.put(reverse('update-research-establishment', args=(self.id,)), self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ResearchEstablishment.objects.get().laboratory, "Modified laboratory")
        self.assertEqual(ResearchEstablishment.objects.get().establishment, "Modified establishment")
        self.assertEqual(ResearchEstablishment.objects.get().commentsEstablishment, "Modified comment establishment")

        #delete research establishment
        response = self.client.delete(reverse('delete-research-establishment',args=(self.id,)))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)