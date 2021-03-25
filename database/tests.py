from django.test import TestCase
from django.utils import timezone

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, force_authenticate
from django.contrib.auth.models import Group

from database.models import *
from community.models import UserProfile

# Create your tests here.

"""
Testing the database with tests data
Bugy for now

"""
class DatabaseTestCase(APITestCase):
    
    def setUp(self):
        #Create profile
        self.data = {"username": "TestUsername","password": "testPassword","email" : "test@email.com"}
        self.client.post(reverse('create-user-profile'), self.data, format='json')
        

        self.id = UserProfile.objects.get().id #get the id from user to update data

        print("User "+str(self.id)+" created with name "+UserProfile.objects.get().username + "\n")
        
        user = UserProfile.objects.get(username='TestUsername')
        self.client.force_authenticate(user=user)




        #Author creation
        self.data = {"user":self.id,"name":"Jean", "lastName":"Martin", "status":"Teacher", "organisation":"School"}
        response = self.client.post(reverse('create-author'), self.data, format='json')
        self.author_id = Author.objects.get().id

        #Source type creation
        self.data = {"typeSource": "Digital document"}
        response = self.client.post(reverse('create-sourceType'), self.data, format='json')
        self.sourceType_id = SourceType.objects.get().id

        #Source creation
        self.data = {"name": "SourceTest", "author": self.author_id, "types": self.sourceType_id, "viability": 1, "conservationPlace": "Museum", "cote": 42}
        response = self.client.post(reverse('create-source'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Source.objects.count(), 1)
        self.assertEqual(Source.objects.get().name, 'SourceTest')
        self.source_id = Source.objects.get().id

    """Date test"""
    def test_date_creation(self):
        
        #Creation
        self.data = {"name": "Date of birth", "date": "2020-11-04"}
        response = self.client.post(reverse('create-date'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Date.objects.count(), 1)
        self.assertEqual(Date.objects.get().name, 'Date of birth')
        self.id = Date.objects.get().id

        #Update
        self.data = {"name": "Date of birth modified", "date": "2019-11-04"}
        response = self.client.put(reverse('update-date', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Date.objects.count(), 1)
        self.assertEqual(Date.objects.get().name, 'Date of birth modified')

        #Delete
        response = self.client.delete(reverse('delete-date', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    """Quality test"""
    def test_quality_creation_update_delete(self):

        #Creation
        self.data = {"name": "Test award", "definition": "Test award allow the user to master all types of test"}
        response = self.client.post(reverse('create-quality'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Quality.objects.count(), 1)
        self.assertEqual(Quality.objects.get().name, 'Test award')
        self.id = Quality.objects.get().id

        #Update
        self.data = {"name": "Modified test award", "definition": "Test award allow the user to master all types of test but modified"}
        response = self.client.put(reverse('update-quality', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Quality.objects.count(), 1)
        self.assertEqual(Quality.objects.get().name, 'Modified test award')

        #Delete
        response = self.client.delete(reverse('delete-quality', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    """Knowledge test"""
    def test_knowledge_creation_update_delete(self):

        #Creation
        self.data = {"name":"Test case", "definition":"Some employee of the company know test case knowledge"}
        response = self.client.post(reverse('create-knowledge'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Knowledge.objects.count(), 1)
        self.assertEqual(Knowledge.objects.get().name, 'Test case')
        self.id = Knowledge.objects.get().id

        #Update
        self.data = {"name":"Test case modified", "definition":"Some employee of the company know test case knowledge"}
        response = self.client.put(reverse('update-knowledge', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Knowledge.objects.count(), 1)
        self.assertEqual(Knowledge.objects.get().name, 'Test case modified')

        #Delete
        response = self.client.delete(reverse('delete-knowledge', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    """
    Source & associates tests
    """

    """Source type test"""
    def test_source_type_creation_update_delete(self):

        #Creation
        

        #Update
        self.data = {"typeSource": "Digital document modified"}
        response = self.client.put(reverse('update-sourceType', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SourceType.objects.count(), 1)
        self.assertEqual(SourceType.objects.get().typeSource, 'Digital document modified')

        #Delete
        response = self.client.delete(reverse('delete-sourceType', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    """Author test"""
    def test_author_creation_update_delete(self):

        #Creation
        

        #Update
        self.data = {"name":"Marie", "lastName":"Martin", "status":"Teacher", "organisation":"School"}
        response = self.client.put(reverse('update-author', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Author.objects.get().name, 'Marie')

        #Delete
        response = self.client.delete(reverse('delete-author', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    """Content test"""
    def test_content_creation_update_delete(self):

        #Creation
        self.data = {"sourceContent":"This is a content of the source"}
        response = self.client.post(reverse('create-content'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Content.objects.count(), 1)
        self.assertEqual(Content.objects.get().sourceContent, 'This is a content of the source')
        self.id = Content.objects.get().id

        #Update
        self.data = {"sourceContent":"This is a modified content of the source"}
        response = self.client.put(reverse('update-content', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Content.objects.count(), 1)
        self.assertEqual(Content.objects.get().sourceContent, 'This is a modified content of the source')

        #Delete
        response = self.client.delete(reverse('delete-content', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    """Files test"""
    def test_file_creation_update_delete(self):

        #Creation
        self.data = {"url":"https://www.django-rest-framework.org/api-guide/serializers/"}
        response = self.client.post(reverse('create-files'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Files.objects.count(), 1)
        self.assertEqual(Files.objects.get().url, 'https://www.django-rest-framework.org/api-guide/serializers/')
        self.id = Files.objects.get().id

        #Update
        self.data = {"url":"https://www.django-rest-framework.org/api-guide/response/"}
        response = self.client.put(reverse('update-files', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Files.objects.count(), 1)
        self.assertEqual(Files.objects.get().url, 'https://www.django-rest-framework.org/api-guide/response/')

        #Delete
        response = self.client.delete(reverse('delete-files', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    """Source test"""
    def test_source_creation_update_delete(self):

        #Update
        self.data = {"name":"SourceTest modified"}
        response = self.client.put(reverse('update-source', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Source.objects.count(), 1)
        self.assertEqual(Source.objects.get().name, 'SourceTest modified')

        #Delete
        response = self.client.delete(reverse('delete-source', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    """
    Place & associates tests
    """

    """Place location test"""
    def test_place_location_creation_update_delete(self):

        #Creation
        self.data = {"street_number": 25, "street_type": "BIS", "street_name": "Wall street", "city": "Test City", "post_code": 123456, "country": "Test Country", "place_said": "The Test Place"}
        response = self.client.post(reverse('create-placeLocation'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PlaceLocation.objects.count(), 1)
        self.assertEqual(PlaceLocation.objects.get().street_number, 25)
        self.id = PlaceLocation.objects.get().id

        #Update
        self.data = {"street_number": 12, "street_type": "TER", "street_name": "Wall no street"}
        response = self.client.put(reverse('update-placeLocation', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PlaceLocation.objects.count(), 1)
        self.assertEqual(PlaceLocation.objects.get().street_name, 'Wall no street')

        #Delete
        response = self.client.delete(reverse('delete-placeLocation', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    """Place type test"""
    def test_place_type_creation_update_delete(self):

        #Creation
        self.data = {"placeType": "Building"}
        response = self.client.post(reverse('create-placeType'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PlaceType.objects.count(), 1)
        self.assertEqual(PlaceType.objects.get().placeType, 'Building')
        self.id = PlaceType.objects.get().id

        #Update
        self.data = {"placeType": "Room"}
        response = self.client.put(reverse('update-placeType', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PlaceType.objects.count(), 1)
        self.assertEqual(PlaceType.objects.get().placeType, 'Room')

        #Delete
        response = self.client.delete(reverse('delete-placeType', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    """Place test"""
    def test_place_creation_update_delete(self):

        #Place location creation
        self.data = {"street_number": 25, "street_type": "BIS", "street_name": "Wall street", "city": "Test City", "post_code": 123456, "country": "Test Country", "place_said": "The Test Place", "source": self.source_id}
        response = self.client.post(reverse('create-placeLocation'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.placeLocation = PlaceLocation.objects.get().id

        #Creation
        self.data = {"name": "Automaton building", "description": "Place where you can run test on automaton", "place_location": self.placeLocation, "longitude": 124.25, "latitude": 133.55, "source": [self.source_id]}
        response = self.client.post(reverse('create-place'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Place.objects.count(), 1)
        self.assertEqual(Place.objects.get().name, 'Automaton building')
        self.id = Place.objects.get().id

        #Update
        self.data = {"name": "Automaton building modified"}
        response = self.client.put(reverse('update-place', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Place.objects.count(), 1)
        self.assertEqual(Place.objects.get().name, 'Automaton building modified')

        #Delete
        response = self.client.delete(reverse('delete-place', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    """Profession test"""
    def test_profession_creation_update_delete(self):

        #Place creation
        self.data = {"name": "Automaton building", "description": "Place where you can run test on automaton", "longitude": 124.25, "latitude": 133.55, "source": [self.source_id]}
        response = self.client.post(reverse('create-place'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.place_id = Place.objects.get().id

        #Creation
        self.data = {"name":"Tester", "definition":"Profession where you eat bugs all day during", "autonomous":False,"place": self.place_id, "source":[self.source_id]}
        response = self.client.post(reverse('create-profession'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profession.objects.count(), 1)
        self.assertEqual(Profession.objects.get().name, 'Tester')
        self.id = Profession.objects.get().id

        #Update
        self.data = {"name":"Tester modified"}
        response = self.client.put(reverse('update-profession', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Profession.objects.count(), 1)
        self.assertEqual(Profession.objects.get().name, 'Tester modified')

        #Delete
        response = self.client.delete(reverse('delete-profession', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    """Collective actor test"""
    def test_collective_actor_creation_update_delete(self):

        #Creation
        self.data = {"name": "Team of young testers", "definition": "Team make for code testing against dark bugs", "source":[self.source_id]}
        response = self.client.post(reverse('create-collectiveActor'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CollectiveActor.objects.count(), 1)
        self.assertEqual(CollectiveActor.objects.get().name, 'Team of young testers')
        self.id = CollectiveActor.objects.get().id

        #Update
        self.data = {"name": "The Master Team"}
        response = self.client.put(reverse('update-collectiveActor', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CollectiveActor.objects.count(), 1)
        self.assertEqual(CollectiveActor.objects.get().name, 'The Master Team')

        #Delete
        response = self.client.delete(reverse('delete-collectiveActor', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    """Abstract object test"""
    def test_abstract_object_creation_update_delete(self):

        #Creation
        self.data = {"name": "Chain of command in the building", "definition": "This allow effective communication and production in the dream testing team", "source": [self.source_id]}
        response = self.client.post(reverse('create-abstractObject'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AbstractObject.objects.count(), 1)
        self.assertEqual(AbstractObject.objects.get().name, 'Chain of command in the building')
        self.id = AbstractObject.objects.get().id

        #Update
        self.data = {"name": "Modified chain of command in the building"}
        response = self.client.put(reverse('update-abstractObject', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(AbstractObject.objects.count(), 1)
        self.assertEqual(AbstractObject.objects.get().name, 'Modified chain of command in the building')

        #Delete
        response = self.client.delete(reverse('delete-abstractObject', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    """
    Social & associate tests
    """

    """Social activity test"""
    def test_social_activity_creation_update_delete(self):

        #Creation
        self.data = {"name": "Ping pong", "definition": "Play ping pong to take a break between working hours", "source": [self.source_id]}
        response = self.client.post(reverse('create-socialActivity'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SocialActivity.objects.count(), 1)
        self.assertEqual(SocialActivity.objects.get().name, 'Ping pong')
        self.id = SocialActivity.objects.get().id

        #Update
        self.data = {"name": "Tenis"}
        response = self.client.put(reverse('update-socialActivity', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SocialActivity.objects.count(), 1)
        self.assertEqual(SocialActivity.objects.get().name, 'Tenis')

        #Delete
        response = self.client.delete(reverse('delete-socialActivity', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    """Sociale link test"""
    def test_social_link_creation_update_delete(self):

        #Creation
        self.data = {"link": "FRIEND", "source": [self.source_id]}
        response = self.client.post(reverse('create-socialLink'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SocialLink.objects.count(), 1)
        self.assertEqual(SocialLink.objects.get().link, 'FRIEND')
        self.id = SocialLink.objects.get().id

        #Update
        self.data = {"link": "CO-WORKERS"}
        response = self.client.put(reverse('update-socialLink', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SocialLink.objects.count(), 1)
        self.assertEqual(SocialLink.objects.get().link, 'CO-WORKERS')

        #Delete
        response = self.client.delete(reverse('delete-socialLink', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    """
    Actor & associate tests
    """

    """Actor test"""
    def test_actor_creation_update_delete(self):

        #Creation
        self.data = {"gender": "Male", "source": [self.source_id]}
        response = self.client.post(reverse('create-actor'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Actor.objects.count(), 1)
        self.assertEqual(Actor.objects.get().gender, 'Male')
        self.id = Actor.objects.get().id

        #Update
        self.data = {"gender": "Female"}
        response = self.client.put(reverse('update-actor', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Actor.objects.count(), 1)
        self.assertEqual(Actor.objects.get().gender, 'Female')

        #Delete
        response = self.client.delete(reverse('delete-actor', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    """Actor name test"""
    def test_name_actor_creation_update_delete(self):

        #Actor creation
        self.data = {"gender": "Male", "source": [self.source_id]}
        response = self.client.post(reverse('create-actor'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.actor_id = Actor.objects.get().id

        #Creation
        self.data = {"name": "Julie","actors": self.actor_id, "last_name": "Denom", "typeOfActor": "Human", "source": [self.source_id]}
        response = self.client.post(reverse('create-nameActor'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(NameActor.objects.count(), 1)
        self.assertEqual(NameActor.objects.get().name, 'Julie')
        self.id = NameActor.objects.get().id

        #Update
        self.data = {"name": "Jean"}
        response = self.client.put(reverse('update-nameActor', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(NameActor.objects.count(), 1)
        self.assertEqual(NameActor.objects.get().name, 'Jean')

        #Delete
        response = self.client.delete(reverse('delete-nameActor', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    """
    Object & associate tests
    """

    """Detail object test"""
    def test_detail_object_creation_update_delete(self):

        #Creation
        self.data = {"detailCaracteristicsObject": "PC", "source": [self.source_id]}
        response = self.client.post(reverse('create-detailCaracteristic'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DetailCaracteristic.objects.count(), 1)
        self.assertEqual(DetailCaracteristic.objects.get().detailCaracteristicsObject, 'PC')
        self.id = DetailCaracteristic.objects.get().id

        #Update
        self.data = {"detailCaracteristicsObject": "Tool"}
        response = self.client.put(reverse('update-detailCaracteristic', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(DetailCaracteristic.objects.count(), 1)
        self.assertEqual(DetailCaracteristic.objects.get().detailCaracteristicsObject, 'Tool')

        #Delete
        response = self.client.delete(reverse('delete-detailCaracteristic', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    """Type object test"""
    def test_type_object_creation_update_delete(self):

        #Creation
        self.data = {"typeObject": "Computer", "source": [self.source_id]}
        response = self.client.post(reverse('create-typeObject'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TypeObject.objects.count(), 1)
        self.assertEqual(TypeObject.objects.get().typeObject, 'Computer')
        self.id = TypeObject.objects.get().id

        #Update
        self.data = {"typeObject": "Welder"}
        response = self.client.put(reverse('update-typeObject', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(TypeObject.objects.count(), 1)
        self.assertEqual(TypeObject.objects.get().typeObject, 'Welder')

        #Delete
        response = self.client.delete(reverse('delete-typeObject', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    """Energy test"""
    def test_energy_creation_update_delete(self):

        #Creation
        self.data = {"energy": "Electricity", "source": [self.source_id]}
        response = self.client.post(reverse('create-energy'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Energy.objects.count(), 1)
        self.assertEqual(Energy.objects.get().energy, 'Electricity')
        self.id = Energy.objects.get().id

        #Update
        self.data = {"energy": "Water"}
        response = self.client.put(reverse('update-energy', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Energy.objects.count(), 1)
        self.assertEqual(Energy.objects.get().energy, 'Water')

        #Delete
        response = self.client.delete(reverse('delete-energy', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    """Object test"""
    def test_object_creation_update_delete(self):

        #Type object creation
        self.data = {"typeObject": "Computer", "source": [self.source_id]}
        response = self.client.post(reverse('create-typeObject'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.typeObject_id = TypeObject.objects.get().id

        #Energy creation
        self.data = {"energy": "Electricity", "source": [self.source_id]}
        response = self.client.post(reverse('create-energy'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.energy_id = Energy.objects.get().id

        #Creation
        self.data = {"name": "Computer of Julie", "definition": "This is the computer Julie is using at work", "brand":"Microsoft", "content": "This computer is really fast since purchase", "type_object": self.typeObject_id, "energy": self.energy_id, "source": [self.source_id]}
        response = self.client.post(reverse('create-object'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Object.objects.count(), 1)
        self.assertEqual(Object.objects.get().name, 'Computer of Julie')
        self.id = Object.objects.get().id

        #Update
        self.data = {"name": "Computer of Jean"}
        response = self.client.put(reverse('update-object', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Object.objects.count(), 1)
        self.assertEqual(Object.objects.get().name, 'Computer of Jean')

        #Delete
        response = self.client.delete(reverse('delete-object', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    """Caracteristic test"""
    def test_caracteristic_creation_update_delete(self):

        #Type object creation
        self.data = {"typeObject": "Computer", "source": [self.source_id]}
        response = self.client.post(reverse('create-typeObject'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.typeObject_id = TypeObject.objects.get().id

        #Energy creation
        self.data = {"energy": "Electricity", "source": [self.source_id]}
        response = self.client.post(reverse('create-energy'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.energy_id = Energy.objects.get().id

        #Object Creation
        self.data = {"name": "Computer of Julie", "definition": "This is the computer Julie is using at work", "brand":"Microsoft", "content": "This computer is really fast since purchase", "type_object": self.typeObject_id, "energy": self.energy_id, "source": [self.source_id]}
        response = self.client.post(reverse('create-object'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.object_id = Object.objects.get().id

        #Creation
        self.data = {"objectCaracteristic": self.object_id, "length": 0.2, "width": 0.01, "height": 0.1, "weight": 1.2, "surface": 0.5, "source": [self.source_id]}
        response = self.client.post(reverse('create-caracteristic'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Caracteristic.objects.count(), 1)
        self.assertEqual(Caracteristic.objects.get().length, 0.2)
        self.id = Caracteristic.objects.get().id

        #Update
        self.data = {"length": 0.3}
        response = self.client.put(reverse('update-caracteristic', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Caracteristic.objects.count(), 1)
        self.assertEqual(Caracteristic.objects.get().length, 0.3)

        #Delete
        response = self.client.delete(reverse('delete-caracteristic', args=(self.id,)), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


        
# class DatabaseTestCaseOld(TestCase):


#     def setUp(self):

#         """ 

#         Source/Date & associates 
        
#         """
#         self.dateTest = Date.objects.create(name="Date of birth", date="2020-11-04")
#         self.authorTest = Author.objects.create(name="Jean", lastName="Martin", status="Teacher", organisation="School")
#         self.sourceTypeTest = SourceType.objects.create(typesSource="Digital document")
#         self.contentTest = Content.objects.create(sourceContent="This is a content of the source")
#         self.urlTest = Url.objects.create(url="https://www.django-rest-framework.org/api-guide/serializers/")
#         self.sourceTest = Source.objects.create(name="SourceTest", author=self.authorTest, types=self.sourceTypeTest, viability=1, conservationPlace="Museum", cote=42)
#         self.sourceTest.save()
#         self.sourceTest.date.add(self.dateTest)
#         self.sourceTest.content.add(self.contentTest)
#         self.sourceTest.url.add(self.urlTest)
        
        
#         """ 
        
#         Quality/Knowledge 
        
#         """
#         self.qualityTest = Quality.objects.create(name="Test award", definition="Test award allow the user to master all types of test")
#         self.knowledgeTest = Knowledge.objects.create(name="Test case", definition="Some employee of the company know test case knowledge")

#         """
        
#         Place & associates 
        
#         """
#         self.placeLocationTest = PlaceLocation.objects.create(street_number=25, street_type="BIS", street_name="Wall street", city="Test City", post_code=123456, country="Test Country", place_said="The Test Place")
#         self.placeTypeTest = PlaceType.objects.create(placeType="Building")
#         self.placeTypeTest.save()
#         self.placeTest = Place.objects.create(name="Automaton building", description="Place where you can run test on automaton", place_location=self.placeLocationTest, longitude=124.25,latitude=133.55)
#         self.placeTest.save()
#         self.placeTest.place_type.add(self.placeTypeTest)
#         self.placeTest.source.add(self.sourceTest)

#         """ 
        
#         Collective Actor 
        
#         """
#         self.collectiveActorTest = CollectiveActor.objects.create(name="Team of young testers", definition="Team make for code testing against dark bugs")
#         self.collectiveActorTest.date.add(self.dateTest)
#         self.collectiveActorTest.quality.add(self.qualityTest)
#         self.collectiveActorTest.knowledge.add(self.knowledgeTest)
#         self.collectiveActorTest.place.add(self.placeTest)
#         self.collectiveActorTest.source.add(self.sourceTest)

#         """ 
        
#         Abstract Object 
        
#         """
#         self.abstractObjectTest = AbstractObject.objects.create(name="Chain of command in the building", definition="This allow effective communication and production in the dream testing team")
#         self.abstractObjectTest.date.add(self.dateTest)
#         self.abstractObjectTest.quality.add(self.qualityTest)
#         self.abstractObjectTest.collectiveActor.add(self.collectiveActorTest)
#         self.abstractObjectTest.knowledge.add(self.knowledgeTest)
#         self.abstractObjectTest.place.add(self.placeTest)
#         self.abstractObjectTest.source.add(self.sourceTest)

#         """ 
        
#         Profession/Social Activities/Social Link 
        
#         """
#         self.professionTest = Profession.objects.create(name="Tester", definition="Profession where you eat bugs all day during", autonomous=False, place=self.placeTest)
#         self.professionTest.abstractObject.add(self.abstractObjectTest)
#         self.professionTest.source.add(self.sourceTest)

#         self.socialActivityTest = SocialActivity.objects.create(name="Ping pong", definition="Play ping pong to take a break between working hours")
#         self.socialActivityTest.place.add(self.placeTest)
#         self.socialActivityTest.source.add(self.sourceTest)

#         """
        
#         Actor & associates 
        
#         """
#         self.actorTest1 = Actor.objects.create(gender='Female')
#         self.actorTest1.profession.add(self.professionTest)
#         self.actorTest1.socialActivities.add(self.socialActivityTest)
#         self.actorTest1.collectiveActors.add(self.collectiveActorTest)
#         self.actorTest1.quality.add(self.qualityTest)
#         # self.actorTest1.socialLink.add(self.social)
#         self.actorTest1.place.add(self.placeTest)
#         self.actorTest1.source.add(self.sourceTest)


#         self.actorTest2 = Actor.objects.create(gender='Male')
#         self.actorTest2.profession.add(self.professionTest)
#         self.actorTest2.socialActivities.add(self.socialActivityTest)
#         self.actorTest2.collectiveActors.add(self.collectiveActorTest)
#         self.actorTest2.quality.add(self.qualityTest)
#         # self.actorTest2.socialLink.add(self.social)
#         self.actorTest2.place.add(self.placeTest)
#         self.actorTest2.source.add(self.sourceTest)

#         self.nameActor1 = NameActor.objects.create(actors=self.actorTest1, name="Julie", last_name="Denom", typeOfActor="Human")
#         self.nameActor2 = NameActor.objects.create(actors=self.actorTest2, name="Mickael", last_name="Denom", typeOfActor="Human")

#         """ 
        
#         Object and associates 
        
#         """
#         self.detailCaracteristicsTest = DetailCaracteristic.objects.create(detailCaracteristicsObject="PC")

#         self.typeObjectTest = TypeObject.objects.create(typeObject="Computer")

#         self.energyTest = Energy.objects.create(energy="Electricity")

#         self.objectTest1 = Object.objects.create(name="Computer of Julie", definition="This is the computer Julie is using at work", brand="Microsoft", content="This computer is really fast since purchase", type_object=self.typeObjectTest, energy=self.energyTest)
#         self.objectTest1.date.add(self.dateTest)
#         self.objectTest1.collectiveActors.add(self.collectiveActorTest)
#         self.objectTest1.actor.add(self.actorTest1)
#         self.objectTest1.abstract_object.add(self.abstractObjectTest)
#         self.objectTest1.place.add(self.placeTest)
#         self.objectTest1.source.add(self.sourceTest)

#         self.objectTest2 = Object.objects.create(name="Computer of Mickael", definition="This is the computer Mickael is using at work", brand="Microsoft", content="This computer is really fast since purchase", type_object=self.typeObjectTest, energy=self.energyTest)
#         self.objectTest2.date.add(self.dateTest)
#         self.objectTest2.collectiveActors.add(self.collectiveActorTest)
#         self.objectTest2.actor.add(self.actorTest2)
#         self.objectTest2.abstract_object.add(self.abstractObjectTest)
#         self.objectTest2.place.add(self.placeTest)
#         self.objectTest2.source.add(self.sourceTest)

#         self.caracteristicTest1 = Caracteristic.objects.create(objectCaracteristic=self.objectTest1, length=0.2, width=0.01, height=0.1, weight=1.2, surface=0.5)
#         self.caracteristicTest1.detail_caracteristics.add(self.detailCaracteristicsTest)
#         self.caracteristicTest1.source.add(self.sourceTest)

#         self.caracteristicTest2 = Caracteristic.objects.create(objectCaracteristic=self.objectTest2, length=0.2, width=0.01, height=0.1, weight=1.2, surface=0.5)
#         self.caracteristicTest2.detail_caracteristics.add(self.detailCaracteristicsTest)
#         self.caracteristicTest2.source.add(self.sourceTest)

#     def test_single_source(self):
#         """
#         Check if the test source has been right created 
#         """ 
#         source_count = Source.objects.count()
#         self.assertEqual(source_count, 1)
    
#     def test_tuple_actor(self):
#         """
#         Check if the actors have been right created 
#         """ 
#         actor_count = Actor.objects.count()
#         self.assertEqual(actor_count, 2)
    
#     def test_tuple_object(self):
#         """
#         Check if objects have been right created 
#         """ 
#         object_count = Object.objects.count()
#         self.assertEqual(object_count, 2)

#     def test_tuple_social_link(self):
#         """
#         Check if actors have socials link added
#         """
#         self.socialLinkTest1 = SocialLink.objects.create(link="FRIEND", actorlink=self.actorTest1)
#         self.actorTest2.socialLink.add(self.socialLinkTest1)

#         self.socialLinkTest2 = SocialLink.objects.create(link="FRIEND", actorlink=self.actorTest2)
#         self.actorTest1.socialLink.add(self.socialLinkTest2)
        
#         socialLink_count = SocialLink.objects.count()
#         self.assertEqual(socialLink_count, 2)