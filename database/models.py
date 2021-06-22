import os
from django.conf import settings
from django.db import models
from django.db.models import fields
from django.db.models.fields.related import ManyToManyField
# from django.utils.translation import Trans
from community.models import UserProfile
"""
Implementation of relationnal models define in static files of the API

To do:
    -update all choices
    -check translation
    -test model
    -test critical test case
    -File upload system
"""

def path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<fileType>/<filename>
    return '{0}/{1}'.format(instance.file_type,filename)


"""
Date table
"""

class Date(models.Model):
    name = models.CharField(max_length=200, blank=True)
    day = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    complement = models.CharField(max_length=200, blank=True)
    duration_date = models.DurationField(null=True, blank=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.name

"""
Quality table
"""

class Quality(models.Model):
    name = models.CharField(max_length=200, blank=True)
    definition = models.CharField(max_length=1000, blank=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.name

"""
Sources & associates tables
"""
# class SourceType(models.Model):
#     typeSource = models.CharField(max_length=200)

#     def __str__(self):
#         return self.typeSource

class Author(models.Model):
    name = models.CharField(max_length=200, blank=True)
    lastName = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True) #To upgrade
    organisation = models.CharField(max_length=200, null=True, blank=True) #To upgrade

    def __str__(self):
        return self.name

class Content(models.Model):
    sourceContent = models.CharField(max_length=10000)

    def __str__(self):
        return self.sourceContent

class Files(models.Model):
    class FileType(models.TextChoices):
        Audio = 'Audio'
        Video = 'Video'
        Cao = 'Cao'
        Image = 'Image'
        Document = 'Document'
    name = models.CharField(max_length=200, null=True, blank=True)
    definition = models.CharField(max_length=1000, null=True, blank=True)
    file_type = models.CharField(choices=FileType.choices, max_length=50,null=True, blank=True)
    file_extension = models.CharField(max_length=20, null=True, blank=True)
    url = models.FileField(upload_to=path,null=True, blank=True)

    def __str__(self):
        return self.url

class Ressource(models.Model):
    class RessourcesField(models.TextChoices):
        Architecture = 'Architecture'
        Production = 'Production'
        Hommes = 'Hommes'
    name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1500, blank=True)
    field = models.CharField(choices=RessourcesField.choices, max_length=20, null=True, blank=True)
    objects_son = models.ManyToManyField('Object', blank=True)
    actors_son = models.ManyToManyField('Actor', blank=True)

class Source(models.Model):
    class Rank(models.IntegerChoices):
        NOTRELIABLE = 0
        RELIABLE  = 1
    name = models.CharField(max_length=500, blank=True)
    date_source = models.ForeignKey(Date, on_delete=models.CASCADE, default=None, blank=True)
    conservation_place = models.CharField(max_length=1000, null=True, blank=True)
    cote = models.CharField(max_length=200, blank=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    editor = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True, related_name='editor')
    
    rights = models.CharField(max_length=250, blank=True)

    url = models.ManyToManyField(Files, blank=True)
    
    registration = models.CharField(max_length=250, blank=True)
    original_registration = models.CharField(max_length=250, blank=True)
    viability = models.IntegerField(choices=Rank.choices, default=0)
    content = models.ManyToManyField(Content, blank=True)
    
    state = models.CharField(max_length=200, blank=True)
    study = models.CharField(max_length=250, blank=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.name

"""
Place & associates tables
"""

class PlaceLocation(models.Model):
    street_number = models.IntegerField(blank=True)
    street_type = models.CharField(max_length=3, null=True, blank=True)
    street_name = models.CharField(max_length=500, blank=True)
    borough = models.IntegerField(null=True, blank=True)
    post_code = models.IntegerField(default=None, null=True, blank=True)
    city = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    place_said = models.CharField(max_length=1000, null=True, blank=True) #Place or said place
    validated = models.BooleanField(default=False)

    def __str__(self):
        return (str(self.street_number) + " " + self.street_name + " " + self.city + " " + self.country)

class PlaceType(models.Model):
    placeType = models.CharField(max_length=500, blank=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.placeType

class Place(models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000, blank=True) #To update
    place_location = models.ForeignKey(PlaceLocation, on_delete=models.CASCADE, default=None, null=True, blank=True)
    longitude = models.FloatField(max_length=9, null=True, blank=True)
    latitude = models.FloatField(max_length=9, null=True, blank=True)
    place_type = models.ManyToManyField(PlaceType, blank=True)
    source = models.ManyToManyField(Source, blank=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.name

"""
Knowledge table
"""

class Knowledge(models.Model):
    name = models.CharField(max_length=200, blank=True)
    definition = models.CharField(max_length=1000, blank=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.name

"""
Collective actor table
"""

class CollectiveActor(models.Model):
    name = models.CharField(max_length=200, blank=True)
    definition = models.CharField(max_length=1000, blank=True)
    date = models.ManyToManyField(Date, blank=True)
    quality = models.ManyToManyField(Quality, blank=True)
    knowledge = models.ManyToManyField(Knowledge, blank=True)
    place = models.ManyToManyField(Place, blank=True)
    source = models.ManyToManyField(Source, blank=True)
    abstract_object = models.ManyToManyField("AbstractObject", blank=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.name

"""
Abstract object table
"""

class AbstractObject(models.Model):
    name = models.CharField(max_length=200, blank=True)
    definition = models.CharField(max_length=1000, blank=True)
    date = models.ManyToManyField(Date, blank=True)
    quality = models.ManyToManyField(Quality, blank=True)
    collectiveActor = models.ManyToManyField(CollectiveActor, blank=True)
    knowledge = models.ManyToManyField(Knowledge, blank=True)
    ab_objects = models.ManyToManyField("Object", blank=True)
    place = models.ManyToManyField(Place, blank=True)
    source = models.ManyToManyField(Source, blank=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.name

"""
Profession table
"""

class Profession(models.Model):
    name = models.CharField(max_length=200, blank=True)
    definition = models.CharField(max_length=1000, blank=True)
    autonomous = models.BooleanField(default=False)
    abstract_object = models.ManyToManyField(AbstractObject, blank=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, default=None, blank=True, null=True,)
    source = models.ManyToManyField(Source, blank=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.name

"""
Social table
"""
class SocialActivity(models.Model):
    name = models.CharField(max_length=200, blank=True)
    definition = models.CharField(max_length=1000, blank=True)
    place = models.ManyToManyField(Place, blank=True)
    source = models.ManyToManyField(Source, blank=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.name


"""
Social link table
"""

class SocialLink(models.Model):
    class SocialLinkType(models.TextChoices):
        FATHER = 'FATHER'
        MOTHER = 'MOTHER'
        SISTER = 'SISTER'
        BROTHER = 'BROTHER'
        FRIEND = 'FRIEND'
        COWORKER = 'CO-WORKERS'

    link = models.CharField(max_length=50, choices=SocialLinkType.choices, blank=True)
    actor_link = models.ForeignKey('Actor', on_delete=models.CASCADE, default=None, null=True, blank=True)
    source = models.ManyToManyField(Source, blank=True)
    validated = models.BooleanField(default=False)

class RelationLink(models.Model):
    class RelationLinkType(models.TextChoices):
        OLD = 'OLD'
        MADEBY = 'MADEBY'
        USE = 'USE'
        CREATE = 'CREATE'
    
    link = models.CharField(max_length=50, choices=RelationLinkType.choices, blank=True)
    object_id = models.ForeignKey('Object', on_delete=models.CASCADE, default=None, null=True, blank=True)
    source = models.ManyToManyField(Source, blank=True)
    validated = models.BooleanField(default=False)

"""
Actor & associate class
"""

class Actor(models.Model):
    class Gender(models.TextChoices):
        Male = 'Homme'
        Female = 'Femme'
        Other = 'Autre'
    
    class LevelOfInstruction(models.TextChoices):
        zero = '0'
        one = '1'
        two = '2'
        three = '3'
        four = '4'
        five = '5'
        X = 'X'
    
    class Categorie(models.TextChoices):
        Hommes = 'Hommes'

    father = ManyToManyField(Ressource, blank=True,related_name='actor_father')

    categorie = models.CharField(max_length=50, choices=Categorie.choices, blank=True)
    domain = models.CharField(max_length=200, blank=True)
    
    building = models.CharField(max_length=500, blank=True)

    name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    profession = models.ForeignKey(Profession,on_delete=models.CASCADE, default=True, blank=True)
    instruction_level = models.CharField(max_length=50, choices=LevelOfInstruction.choices, blank=True)
    
    birth_date = models.ForeignKey(Date, on_delete=models.CASCADE, default=True, blank=True, related_name='birth')    
    birth_place = models.ForeignKey(Place, on_delete=models.CASCADE, default=None, blank=True, related_name='birth_place')
    # birth_place = models.ForeignKey(Place, on_delete=models.CASCADE, default=None, blank=True, related_name='birth_place')

    gender = models.CharField(max_length=50, choices=Gender.choices, blank=True)
    arrival_date = models.ForeignKey(Date, on_delete=models.CASCADE, default=None, blank=True, related_name='arrival')
    departure_date = models.ForeignKey(Date, on_delete=models.CASCADE, default=None, blank=True)
    nationality = models.CharField(max_length=200, blank=True)
    living_place = models.ForeignKey(Place, on_delete=models.CASCADE, default=None, blank=True)
    
    home_status = models.CharField(max_length=200, blank=True)
    home_size = models.IntegerField(blank=True, null=True)
    wedding_date = models.ForeignKey(Date, on_delete=models.CASCADE, default=None, blank=True, related_name='wedding_date')
    wedding_place = models.ForeignKey(Place, on_delete=models.CASCADE, default=None, blank=True, related_name='wedding_place')
    
    wedding_name = models.CharField(max_length=200, blank=True)
    wedding_lastName = models.CharField(max_length=200, blank=True)
    death_date = models.ForeignKey(Date, on_delete=models.CASCADE, default=None, blank=True, related_name='death_date')
    death_place = models.ForeignKey(Place, on_delete=models.CASCADE, default=None, blank=True, related_name='death_place')
    

    commentary = models.CharField(max_length=1000, blank=True)
    
    
    #Not used for TTM
    socialActivities = models.ManyToManyField(SocialActivity, blank=True)
    collectiveActors = models.ManyToManyField(CollectiveActor, blank=True)
    quality = models.ManyToManyField(Quality, blank=True)
    socialLink = models.ManyToManyField(SocialLink, blank=True)
    knowledge = models.ManyToManyField(Knowledge, blank=True)
   
    source = models.ManyToManyField(Source, blank=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class NameActor(models.Model):
    actors = models.ForeignKey(Actor, on_delete=models.CASCADE, default=None, blank=True)
    name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    typeOfActor = models.CharField(max_length=200, null=True, blank=True)
    source = models.ManyToManyField(Source, blank=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return (self.name + " " + self.last_name)


"""
Object and associate tables
"""
class DetailCaracteristic(models.Model):
    detailCaracteristicsObject = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.detailCaracteristicsObject


class TypeObject(models.Model):
    typeObject = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.typeObject

class Energy(models.Model):
    energy = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.energy



class Object(models.Model):
    class categorie_type(models.TextChoices):
        Architecture = 'Architecture'
        Production = 'Production'
        Hommes = 'Hommes'
        Urbanisme = 'Urbanisme'

    class type_object(models.TextChoices):
        building = 'building'
        machine = 'machine'

    class period_duration(models.TextChoices):
        firstNine = '1er quart 19e siècle'
        secondNine = '2e quart 19e siècle'
        thirdNine = '3e quart 19e siècle'
        fourthNine = '4e quart 19e siècle'
        firstTwenty = '1er quart 20e siècle'
        secondTwenty = '2e quart 20e siècle'
        thirdTwenty = '3e quart 20e siècle'
        fourthTwenty = '4e quart 20e siècle'
        firstTwentyOne = '1er quart 21e siècle'

    father = ManyToManyField(Ressource, blank=True,related_name='object_father')

    name = models.CharField(max_length=200, blank=True)
    categorie = models.CharField(max_length=50, choices=categorie_type.choices, blank=True)
    domain = models.CharField(max_length=200, blank=True)
    lower_categorie = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    abstract_object = models.ManyToManyField(AbstractObject, blank=True)
    
    fk_typologie = models.ForeignKey("Typologie", on_delete=models.CASCADE, default=None, null=True, blank=True)
    period = models.CharField(max_length=200, choices=period_duration.choices, blank=True)
    date = models.ManyToManyField(Date, blank=True)
    place = models.ManyToManyField(Place, blank=True)
    type_object = models.ForeignKey(TypeObject, on_delete=models.CASCADE, default=None, blank=True)
    collective_actors = models.ManyToManyField(CollectiveActor, blank=True)
    actor = models.ManyToManyField(Actor, blank=True)
    
    energy = models.ForeignKey(Energy, on_delete=models.CASCADE, default=None, null=True, blank=True)
    
    source = models.ManyToManyField(Source,blank=True)
    content = models.CharField(max_length=1000, null=True, blank=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Typologie(models.Model):
    # Typologie
    plan = models.CharField(max_length=500, blank=True)
    wall = models.CharField(max_length=500, blank=True)
    roof = models.CharField(max_length=500, blank=True)
    floor = models.IntegerField(blank=True)
    surface = models.IntegerField(blank=True)
    light = models.CharField(max_length=500, blank=True)
    materials = models.CharField(max_length=500, blank=True)

class Caracteristic(models.Model):
    objectCaracteristic = models.ForeignKey(Object, on_delete=models.CASCADE,blank=True)
    length = models.FloatField(null=True, blank=True, default=None)
    width = models.FloatField(null=True, blank=True, default=None)
    height = models.FloatField(null=True, blank=True, default=None)
    weight = models.FloatField(null=True, blank=True, default=None)
    surface = models.FloatField(null=True, blank=True, default=None)
    detail_caracteristics = models.ManyToManyField(DetailCaracteristic, blank=True)

    def __str__(self):
        return ("Caracteristics of " + self.objectCaracteristic.name)

class ModifyAttribute(models.Model):
    class Table(models.TextChoices):
        Date = 'Date'
        Quality = 'Quality'
        SourceType = 'SourceType'
        Author = 'Author'
        Content = 'Content'
        Url = 'Url'
        Source = 'Source'
        PlaceLocation = 'PlaceLocation'
        PlaceType = 'PlaceType'
        Place = 'Place'
        Knowledge = 'Knowledge'
        CollectiveActor = 'CollectiveActor'
        AbstractObject = 'AbstractObject'
        Profession = 'Profession'
        SocialActivity = 'SocialActivity'
        SocialLink = 'SocialLink'
        Actor = 'Actor'
        NameActor = 'NameActor'
        DetailCaracteristic = 'DetailCaracteristic'
        TypeObject = 'TypeObject'
        Energy = 'Energy'
        Object = 'Object'
        Caracteristic = 'Caracteristic'
    table = models.CharField(max_length=250, choices=Table.choices, blank=True)
    field_value = models.CharField(max_length=250, blank=True)
    instance_value = models.IntegerField(blank=True)
    content = models.CharField(max_length=10000, blank=True)

    def __str__(self):
        return self.content