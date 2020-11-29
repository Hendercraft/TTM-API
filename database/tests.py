from django.test import TestCase
from django.utils import timezone

from database.models import *

# Create your tests here.

"""
Testing the database with tests data
Bugy for now
"""
class DatabaseTestCase(TestCase):


    def setUp(self):

        """ 

        Source/Date & associates 
        
        """
        self.dateTest = Date.objects.create(name="Date of birth", date="2020-11-04")
        self.authorTest = Author.objects.create(name="Jean", lastName="Martin", status="Teacher", organisation="School")
        self.sourceTypeTest = SourceType.objects.create(typesSource="Digital document")
        self.contentTest = Content.objects.create(sourceContent="This is a content of the source")
        self.urlTest = Url.objects.create(url="https://www.django-rest-framework.org/api-guide/serializers/")
        self.sourceTest = Source.objects.create(name="SourceTest", author=self.authorTest, types=self.sourceTypeTest, viability=1, conservationPlace="Museum", cote=42)
        self.sourceTest.save()
        self.sourceTest.date.add(self.dateTest)
        self.sourceTest.content.add(self.contentTest)
        self.sourceTest.url.add(self.urlTest)
        
        
        """ 
        
        Quality/Knowledge 
        
        """
        self.qualityTest = Quality.objects.create(name="Test award", definition="Test award allow the user to master all types of test")
        self.knowledgeTest = Knowledge.objects.create(name="Test case", definition="Some employee of the company know test case knowledge")

        """
        
        Place & associates 
        
        """
        self.placeLocationTest = PlaceLocation.objects.create(street_number=25, street_type="BIS", street_name="Wall street", city="Test City", post_code=123456, country="Test Country", place_said="The Test Place")
        self.placeTypeTest = PlaceType.objects.create(placeType="Building")
        self.placeTypeTest.save()
        self.placeTest = Place.objects.create(name="Automaton building", description="Place where you can run test on automaton", place_location=self.placeLocationTest, longitude=124.25,latitude=133.55)
        self.placeTest.save()
        self.placeTest.place_type.add(self.placeTypeTest)
        self.placeTest.source.add(self.sourceTest)

        """ 
        
        Collective Actor 
        
        """
        self.collectiveActorTest = CollectiveActor.objects.create(name="Team of young testers", definition="Team make for code testing against dark bugs")
        self.collectiveActorTest.date.add(self.dateTest)
        self.collectiveActorTest.quality.add(self.qualityTest)
        self.collectiveActorTest.knowledge.add(self.knowledgeTest)
        self.collectiveActorTest.place.add(self.placeTest)
        self.collectiveActorTest.source.add(self.sourceTest)

        """ 
        
        Abstract Object 
        
        """
        self.abstractObjectTest = AbstractObject.objects.create(name="Chain of command in the building", definition="This allow effective communication and production in the dream testing team")
        self.abstractObjectTest.date.add(self.dateTest)
        self.abstractObjectTest.quality.add(self.qualityTest)
        self.abstractObjectTest.collectiveActor.add(self.collectiveActorTest)
        self.abstractObjectTest.knowledge.add(self.knowledgeTest)
        self.abstractObjectTest.place.add(self.placeTest)
        self.abstractObjectTest.source.add(self.sourceTest)

        """ 
        
        Profession/Social Activities/Social Link 
        
        """
        self.professionTest = Profession.objects.create(name="Tester", definition="Profession where you eat bugs all day during", autonomous=False, place=self.placeTest)
        self.professionTest.abstractObject.add(self.abstractObjectTest)
        self.professionTest.source.add(self.sourceTest)

        self.socialActivityTest = SocialActivity.objects.create(name="Ping pong", definition="Play ping pong to take a break between working hours")
        self.socialActivityTest.place.add(self.placeTest)
        self.socialActivityTest.source.add(self.sourceTest)

        """
        
        Actor & associates 
        
        """
        self.actorTest1 = Actor.objects.create(gender='Female')
        self.actorTest1.profession.add(self.professionTest)
        self.actorTest1.socialActivities.add(self.socialActivityTest)
        self.actorTest1.collectiveActors.add(self.collectiveActorTest)
        self.actorTest1.quality.add(self.qualityTest)
        # self.actorTest1.socialLink.add(self.social)
        self.actorTest1.place.add(self.placeTest)
        self.actorTest1.source.add(self.sourceTest)


        self.actorTest2 = Actor.objects.create(gender='Male')
        self.actorTest2.profession.add(self.professionTest)
        self.actorTest2.socialActivities.add(self.socialActivityTest)
        self.actorTest2.collectiveActors.add(self.collectiveActorTest)
        self.actorTest2.quality.add(self.qualityTest)
        # self.actorTest2.socialLink.add(self.social)
        self.actorTest2.place.add(self.placeTest)
        self.actorTest2.source.add(self.sourceTest)

        self.nameActor1 = NameActor.objects.create(actors=self.actorTest1, name="Julie", last_name="Denom", typeOfActor="Human")
        self.nameActor2 = NameActor.objects.create(actors=self.actorTest2, name="Mickael", last_name="Denom", typeOfActor="Human")

        """ 
        
        Object and associates 
        
        """
        self.detailCaracteristicsTest = DetailCaracteristic.objects.create(detailCaracteristicsObject="PC")

        self.typeObjectTest = TypeObject.objects.create(typeObject="Computer")

        self.energyTest = Energy.objects.create(energy="Electricity")

        self.objectTest1 = Object.objects.create(name="Computer of Julie", definition="This is the computer Julie is using at work", brand="Microsoft", content="This computer is really fast since purchase", type_object=self.typeObjectTest, energy=self.energyTest)
        self.objectTest1.date.add(self.dateTest)
        self.objectTest1.collectiveActors.add(self.collectiveActorTest)
        self.objectTest1.actor.add(self.actorTest1)
        self.objectTest1.abstract_object.add(self.abstractObjectTest)
        self.objectTest1.place.add(self.placeTest)
        self.objectTest1.source.add(self.sourceTest)

        self.objectTest2 = Object.objects.create(name="Computer of Mickael", definition="This is the computer Mickael is using at work", brand="Microsoft", content="This computer is really fast since purchase", type_object=self.typeObjectTest, energy=self.energyTest)
        self.objectTest2.date.add(self.dateTest)
        self.objectTest2.collectiveActors.add(self.collectiveActorTest)
        self.objectTest2.actor.add(self.actorTest2)
        self.objectTest2.abstract_object.add(self.abstractObjectTest)
        self.objectTest2.place.add(self.placeTest)
        self.objectTest2.source.add(self.sourceTest)

        self.caracteristicTest1 = Caracteristic.objects.create(objectCaracteristic=self.objectTest1, length=0.2, width=0.01, height=0.1, weight=1.2, surface=0.5)
        self.caracteristicTest1.detail_caracteristics.add(self.detailCaracteristicsTest)
        self.caracteristicTest1.source.add(self.sourceTest)

        self.caracteristicTest2 = Caracteristic.objects.create(objectCaracteristic=self.objectTest2, length=0.2, width=0.01, height=0.1, weight=1.2, surface=0.5)
        self.caracteristicTest2.detail_caracteristics.add(self.detailCaracteristicsTest)
        self.caracteristicTest2.source.add(self.sourceTest)

    def test_single_source(self):
        """
        Check if the test source has been right created 
        """ 
        source_count = Source.objects.count()
        self.assertEqual(source_count, 1)
    
    def test_tuple_actor(self):
        """
        Check if the actors have been right created 
        """ 
        actor_count = Actor.objects.count()
        self.assertEqual(actor_count, 2)
    
    def test_tuple_object(self):
        """
        Check if objects have been right created 
        """ 
        object_count = Object.objects.count()
        self.assertEqual(object_count, 2)

    def test_tuple_social_link(self):
        """
        Check if actors have socials link added
        """
        self.socialLinkTest1 = SocialLink.objects.create(link="FRIEND", actorlink=self.actorTest1)
        self.actorTest2.socialLink.add(self.socialLinkTest1)

        self.socialLinkTest2 = SocialLink.objects.create(link="FRIEND", actorlink=self.actorTest2)
        self.actorTest1.socialLink.add(self.socialLinkTest2)
        
        socialLink_count = SocialLink.objects.count()
        self.assertEqual(socialLink_count, 2)