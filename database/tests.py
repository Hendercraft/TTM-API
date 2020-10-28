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

        """ Source/Date & associates """
        time = timezone.now()
        self.dateTest = Date.objects.create(name="Date of birth", date=time)
        self.authorTest = Author.objects.create(name="Jean", lastName="Martin", status="Teacher", organisation="School")
        self.sourceTypeTest = SourceTypes.objects.create(typesSource="Digital document")
        self.contentTest = Content.objects.create(sourceContent="This is a content of the source")
        self.urlTest = Url.objects.create(url="https://www.django-rest-framework.org/api-guide/serializers/")
        self.sourceTest = Source.objects.create(name="SourceTest", author=self.authorTest, date=self.dateTest, types=self.sourceTypeTest, content=self.contentTest, url=self.urlTest, viability=1, conservationPlace="Museum", cote=42)

        """ Quality/Knowledge """
        qualityTest = Quality.objects.create(name="Test award", definition="Test award allow the user to master all types of test")
        knowledgeTest = Knowledge.objects.create(name="Test case", definition="Some employee of the company know test case knowledge")

        """ Place & associates """
        placeLocationTest = PlaceLocation.objects.create(street_number=25, street_type="BIS", street_name="Wall street", city="Test City", post_code=123456, country="Test Country", lieu_dit="The Test Place")
        placeTypeTest = PlaceType.objects.create(placeType="Building")
        placeTest = Place.objects.create(name="Automaton building", description="Place where you can run test on automaton", place_location=placeLocationTest, longitude=124.25,latitude=133.55, place_type=placeTypeTest, source=sourceTest)
        
        """ Collective Actor """
        collectiveActorTest = CollectiveActor.objects.create(name="Team of young testers", definition="Team make for code testing against dark bugs", date=dateTest, quality=qualityTest, knowledge=knowledgeTest, place=placeTest, source=sourceTest)

        """ Abstract Object """
        abstractObjectTest = AbstractObject.objects.create(name="Chain of command in the building", definition="This allow effective communication and production in the dream testing team", date=dateTest, quality=qualityTest, collectiveActor=collectiveActorTest, knowledge=knowledgeTest, place=placeTest, source=sourceTest)
        
        """ Profession/Social Activities/Social Link """
        professionTest = Profession.objects.create(name="Tester", definition="Profession where you eat bugs all day during", autonomous=False, abstractobjects=abstractObjectTest, place=placeTest, source=sourceTest)

        socialActivityTest = SocialActivitie.objects.create(name="Ping pong", definition="Play ping pong to take a break between working hours", place=placeTest, source=sourceTest)


        """ Actor & associates """
        actorTest1 = Actor.objects.create(gender='Female', profession=professionTest, socialActivities=socialActivityTest, collectiveActors=collectiveActorTest, quality=qualityTest, place=placeTest, source=sourceTest)
        actorTest2 = Actor.objects.create(gender='Male', profession=professionTest, socialActivities=socialActivityTest, collectiveActors=collectiveActorTest, quality=qualityTest, place=placeTest, source=sourceTest)

        nameActor1 = NameActor.objects.create(actors=actorTest1, name="Julie", last_name="Denom", typeOfActor="Human")
        nameActor2 = NameActor.objects.create(actors=actorTest2, name="Mickael", last_name="Denom", typeOfActor="Human")

        """ Object and associates """
        detailCaracteristicsTest = DetailCaracteristics.objects.create(detailCaracteristicsObject="PC")

        typeObjectTest = TypeObject.objects.create(typeObject="Computer")

        energyTest = Energy.objects.create(energy="Electricity")

        objectTest1 = Object.objects.create(name="Computer of Julie", definition="This is the computer Julie is using at work", brand="Microsoft", content="This computer is really fast since purchase", type_object=typeObjectTest, collectiveActors=collectiveActorTest, actor=actorTest1, abstract_object=abstractObjectTest, energy=energyTest, place=placeTest, source=sourceTest)
        objectTest2 = Object.objects.create(name="Computer of Mickael", definition="This is the computer Mickael is using at work", brand="Microsoft", content="This computer is really fast since purchase", type_object=typeObjectTest, collectiveActors=collectiveActorTest, actor=actorTest2, abstract_object=abstractObjectTest, energy=energyTest, place=placeTest, source=sourceTest)

        caracteristicTest1 = Caracteristic.objects.create(objectCaracteristic=objectTest1, length=0.2, width=0.01, height=0.1, weight=1.2, detail_caracteristics=detailCaracteristicsTest, surface=0.5, source=sourceTest)
        caracteristicTest2 = Caracteristic.objects.create(objectCaracteristic=objectTest2, length=0.2, width=0.01, height=0.1, weight=1.2, detail_caracteristics=detailCaracteristicsTest, surface=0.5, source=sourceTest)

    def test_get_objects_by_actors(self):
        """ 
        Get all objects filtered by actors 
        """

        list_object = Object.objects.all()
        """
        self.assertQuerysetEqual(
            len(list_object),2
        )
        """