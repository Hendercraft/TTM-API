from django.db import models
from community.models import UserProfile
"""
Implementation of relationnal models define in static files of the API

To do:
    -update all choices
    -check translation
    -test model
    -test critical test case
"""


"""
Date table
"""

class Date(models.Model):
    name = models.CharField(max_length=200, blank=True)
    date = models.DateField(null=True, blank=True)
    duration_date = models.DurationField(null=True, blank=True)
    source_date = models.ManyToManyField("Source", blank=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.name

"""
Quality table
"""

class Quality(models.Model):
    name = models.CharField(max_length=200, blank=True)
    definition = models.CharField(max_length=1000, blank=True)
    source_quality = models.ManyToManyField("Source", blank=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.name

"""
Sources & associates tables
"""
class SourceType(models.Model):
    typeSource = models.CharField(max_length=200)

    def __str__(self):
        return self.typesSource

class Author(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
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

class Url(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    definition = models.CharField(max_length=1000, null=True, blank=True)
    url = models.URLField()

    def __str__(self):
        return self.url

class Source(models.Model):
    class Rank(models.IntegerChoices):
        NOTRELIABLE = 0
        RELIABLE  = 1
    name = models.CharField(max_length=500, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    date_source = models.ManyToManyField(Date, blank=True)
    types = models.ForeignKey(SourceType, on_delete=models.CASCADE, blank=True)
    content = models.ManyToManyField(Content, blank=True)
    url = models.ManyToManyField(Url, blank=True)
    viability = models.IntegerField(choices=Rank.choices, default=0)
    conservationPlace = models.CharField(max_length=1000, null=True, blank=True)
    cote = models.CharField(max_length=200, blank=True) #To translate
    state = models.CharField(max_length=200, blank=True)
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
    abstractObject = models.ManyToManyField("AbstractObject", blank=True)
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
    objects = models.ManyToManyField("Object", blank=True)
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
    abstractObject = models.ManyToManyField(AbstractObject, blank=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, default=None)
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
    actorlink = models.ForeignKey('Actor', on_delete=models.CASCADE, default=None, null=True, blank=True)
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
        Male = 'Male'
        Female = 'Female'
        Other = 'Other'
    gender = models.CharField(max_length=50, choices=Gender.choices, blank=True)
    profession = models.ManyToManyField(Profession, blank=True)
    socialActivities = models.ManyToManyField(SocialActivity, blank=True)
    collectiveActors = models.ManyToManyField(CollectiveActor, blank=True)
    quality = models.ManyToManyField(Quality, blank=True)
    socialLink = models.ManyToManyField(SocialLink, blank=True)
    place = models.ManyToManyField(Place, blank=True)
    knowledge = models.ManyToManyField(Knowledge, blank=True)
    source = models.ManyToManyField(Source, blank=True)
    validated = models.BooleanField(default=False)


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
    source = models.ManyToManyField(Source, blank=True)
    validated = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.detailCaracteristicsObject


class TypeObject(models.Model):
    typeObject = models.CharField(max_length=500, blank=True)
    source = models.ManyToManyField(Source, blank=True)
    validated = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.typeObject

class Energy(models.Model):
    energy = models.CharField(max_length=200, blank=True)
    source = models.ManyToManyField(Source, blank=True)
    validated = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.energy

class Object(models.Model):
    name = models.CharField(max_length=200, blank=True)
    definition = models.CharField(max_length=1000, blank=True)
    brand = models.CharField(max_length=500, null=True, blank=True)
    content = models.CharField(max_length=1000, null=True, blank=True)
    date = models.ManyToManyField(Date, blank=True)
    type_object = models.ForeignKey(TypeObject, on_delete=models.CASCADE, default=None, blank=True)
    collectiveActors = models.ManyToManyField(CollectiveActor, blank=True)
    actor = models.ManyToManyField(Actor, blank=True)
    abstract_object = models.ManyToManyField(AbstractObject, blank=True)
    energy = models.ForeignKey(Energy, on_delete=models.CASCADE, default=None, null=True, blank=True)
    place = models.ManyToManyField(Place, blank=True)
    source = models.ManyToManyField(Source,blank=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Caracteristic(models.Model):
    objectCaracteristic = models.ForeignKey(Object, on_delete=models.CASCADE,blank=True)
    length = models.FloatField(null=True, blank=True, default=None)
    width = models.FloatField(null=True, blank=True, default=None)
    height = models.FloatField(null=True, blank=True, default=None)
    weight = models.FloatField(null=True, blank=True, default=None)
    surface = models.FloatField(null=True, blank=True, default=None)
    detail_caracteristics = models.ManyToManyField(DetailCaracteristic, blank=True)
    source = models.ManyToManyField(Source, blank=True)
    validated = models.BooleanField(default=False)

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