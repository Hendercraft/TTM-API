from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User, Group 

from .models import Profile, Discipline, ResearchField, ResearchEstablishment

class CommunityTestCase(APITestCase):
    
    def test_create_update_retrieve_delete_profile(self):
        """
        Test profile create_update_retrieve_delete
        """
        #create profile
        url = reverse('create-user-profile')
        data = {"username": "TestUsername","password": "testPassword","email" : "test@email.com"}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(User.objects.count(), 1)
        
        #update profile
        id = User.objects.get().id #get the id from user to update data
        url = reverse('update-user-profile', args=(id,))
        data = {
            "user":
            {
                "username": "ModifiedTestUsername","email" : "testmodified@email.com"
                }
            }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get().username, "ModifiedTestUsername")

        #Retrieve profile
        url_retrieve = reverse('retrieve-user-profile', args=(id,))
        response = self.client.get(url_retrieve)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #delete profile
        url_delete = reverse('delete-user-profile',args=(id,))
        response = self.client.delete(url_delete)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_create_update_retrieve_delete_discipline(self):
        """
        Test discipline create_update_retrieve_delete
        """
        #Create profile
        url = reverse('create-user-profile')
        data = {"username": "TestUsername","password": "testPassword","email" : "test@email.com"}
        response = self.client.post(url, data, format='json')
        id=User.objects.get().id #get the id from user to update data
        
        #Create discipline
        url = reverse('create-discipline')
        data = {"discipline": "Test discipline","commentsDiscipline": "Test comment discipline"}
        response = self.client.post(url, data, format='json')

        # "user": id,
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Discipline.objects.count(), 1)
        self.assertEqual(Discipline.objects.get().discipline, 'Test discipline')

        #Retrieve discipline
        url_retrieve = reverse('retrieve-discipline', args=(id,))
        response = self.client.get(url_retrieve)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #update discipline
        url_update = reverse('update-discipline', args=(id,))
        data = {"discipline": "ModifiedDiscipline","commentsDiscipline" : "Modified Comment discipline"}
        response = self.client.put(url_update, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Discipline.objects.get().discipline, "ModifiedDiscipline")
        self.assertEqual(Discipline.objects.get().commentsDiscipline, "Modified Comment discipline")

        #delete discipline
        url_delete = reverse('delete-discipline',args=(id,))
        response = self.client.delete(url_delete)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_create_update_retrieve_delete_research_field(self):
        """
        Test research field create_update_retrieve_delete
        """
        #Create profile
        url = reverse('create-user-profile')
        data = {"username": "TestUsername","password": "testPassword","email" : "test@email.com"}
        response = self.client.post(url, data, format='json')
        id=User.objects.get().id #get the id from user to update data

        url = reverse('create-research-field')
        data = {"user": id,"researchField": "Test research field","commentsResearch": "Test comment research"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ResearchField.objects.count(), 1)
        self.assertEqual(ResearchField.objects.get().researchField, 'Test research field')

        #Retrieve research field
        url_retrieve = reverse('retrieve-research-field', args=(1,))
        response = self.client.get(url_retrieve)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #update research field
        url_update = reverse('update-research-field', args=(1,))
        data = {"researchField": "Modified research field","commentsResearch" : "Modified comment research"}
        response = self.client.put(url_update, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ResearchField.objects.get().researchField, "Modified research field")
        self.assertEqual(ResearchField.objects.get().commentsResearch, "Modified comment research")

        #delete research field
        url_delete = reverse('delete-research-field',args=(1,))
        response = self.client.delete(url_delete)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_update_retrieve_delete_research_establishment(self):
        """
        Test research establishment create_update_retrieve_delete
        """
        #Create profile
        url = reverse('create-user-profile')
        data = {"username": "TestUsername","password": "testPassword","email" : "test@email.com"}
        response = self.client.post(url, data, format='json')
        id=User.objects.get().id #get the id from user to update data

        url = reverse('create-research-establishment')
        data = {"user": id,"laboratory": "Test laboratory","establishment": "Test establishment","commentsEstablishment": "Test comment establishment"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ResearchEstablishment.objects.count(), 1)
        self.assertEqual(ResearchEstablishment.objects.get().laboratory, 'Test laboratory')

        #Retrieve research establishment
        url_retrieve = reverse('retrieve-research-establishment', args=(1,))
        response = self.client.get(url_retrieve)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #update research establishment
        url_update = reverse('update-research-establishment', args=(1,))
        data = {"laboratory": "Modified laboratory","establishment" : "Modified establishment", "commentsEstablishment": "Modified comment establishment"}
        response = self.client.put(url_update, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ResearchEstablishment.objects.get().laboratory, "Modified laboratory")
        self.assertEqual(ResearchEstablishment.objects.get().establishment, "Modified establishment")
        self.assertEqual(ResearchEstablishment.objects.get().commentsEstablishment, "Modified comment establishment")

        #delete research establishment
        url_delete = reverse('delete-research-establishment',args=(1,))
        response = self.client.delete(url_delete)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    
