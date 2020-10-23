from django.db import models

# Create your models here.
"""
Implementation of relationnal models define in static files of the API

To do:
    -check link (foreign key)
    -put __str__ to all models
    -update all choices
    -check translation
    -test model
    -test critical test case
"""

"""
Date table
"""

class Date(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    duration_date = models.DurationField()

    def __str__(self):
        return self.name

"""
Quality table
"""

class Quality(models.Model):
    name = models.CharField(max_length=200)
    definition = models.CharField(max_length=200)

    def __str__(self):
        return self.name

"""
Sources & associates tables
"""
class Types(models.Model):
    class TypeChoice(models.TextChoices):
        SCAN = 'SCAN'
        DDD_MODELS = '3D MODEL'
        
    types_source = models.CharField(max_length=10,choices=TypeChoice.choices)

    def __str__(self):
        return self.TypeChoice

class Author(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    status = models.CharField(max_length=200) #To upgrade
    organisation = models.CharField(max_length=200) #To upgrade

    def __str__(self):
        return self.name

class Content(models.Model):
    source_content = models.CharField(max_length=1000) 

class Url(models.Model):
    url = models.URLField()

class Source(models.Model):
    class Rank(models.IntegerChoices):
        NOTRELIABLE = 0
        RELIABLE  = 1
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    types = models.ForeignKey(Types, on_delete=models.CASCADE)
    content = models.ManyToManyField(Content)
    url = models.ManyToManyField(Url)
    viability = models.IntegerField(choices=Rank.choices)
    conservation_place = models.CharField(max_length=500)
    cote = models.CharField(max_length=200) #To translate
    

    def __str__(self):
        return self.name

"""
Place & associates tables
"""

class PlaceLocation(models.Model):
    street_number = models.IntegerField()
    street_type = models.CharField(max_length=3)
    street_name = models.CharField(max_length=200) #To update
    city = models.CharField(max_length=100)
    post_code = models.IntegerField()
    country = models.CharField(max_length=100)
    lieu_dit = models.CharField(max_length=200)

class PlaceType(models.Model):
    class TypePlace(models.TextChoices):
        BUILDING = 'BUILDING'
    placeType = models.CharField(max_length=10,choices=TypePlace.choices)

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500) #To update
    place_location = models.ForeignKey(PlaceLocation, on_delete=models.CASCADE, default=None)
    longitude = models.FloatField()
    latitude = models.FloatField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    place_type = models.ForeignKey(PlaceType, on_delete=models.CASCADE, default=None) 

    def __str__(self):
        return self.name

"""
Knowledge table
"""

class Knowledge(models.Model):
    name = models.CharField(max_length=200)
    definition = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

"""
Collective actor table
"""

class CollectiveActor(models.Model):
    name = models.CharField(max_length=200)
    definition = models.CharField(max_length=1000)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    knowledge = models.ForeignKey(Knowledge, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

"""
Abstract object table
"""

class AbstractObject(models.Model):
    name = models.CharField(max_length=200)
    definition = models.CharField(max_length=1000)
    collectiveActor = models.ManyToManyField(CollectiveActor)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE)
    knowledge = models.ForeignKey(Knowledge, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

"""
Profession table
"""

class Profession(models.Model):
    name = models.CharField(max_length=200)
    definition = models.CharField(max_length=500)
    autonomous = models.BooleanField(default=False)
    abstractobjects = models.ManyToManyField(AbstractObject)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    source = models.ManyToManyField(Source)

    def __str__(self):
        return self.name

"""
Social table
"""
class Social(models.Model):
    name = models.CharField(max_length=200)
    definition = models.CharField(max_length=500)
    place = models.ManyToManyField(Place)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


"""
Social link table
"""

class SocialLink(models.Model):
    class SocialLinkType(models.TextChoices):
        FATHER = 'FATHER'
        MOTHER = 'MOTHER'
    socialLink = models.CharField(max_length=50, choices=SocialLinkType.choices)


"""
Actor & associate class
"""


class Actor(models.Model):
    sexe = models.BooleanField()
    profession = models.ManyToManyField(Profession)
    social = models.ForeignKey(Social, on_delete=models.CASCADE)
    collectiveActors = models.ForeignKey(CollectiveActor, on_delete=models.CASCADE)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE)
    socialLink = models.ForeignKey(SocialLink, on_delete=models.CASCADE)
    place = models.ManyToManyField(Place)
    source = models.ManyToManyField(Source)

#    def __str__(self):  Return id of the actor
#        return self.name

class NameActor(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return (self.name + " " + self.last_name)


"""
Object and associate tables
"""
class DetailCaracteristics(models.Model):
    class ObjectCaracteristics(models.TextChoices):
        DETAIL1 = 'DETAIL1'
    detailCaracteristicsObject = models.CharField(max_length=50, choices=ObjectCaracteristics.choices)

class Caracteristics(models.Model):
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    detail_caracteristics = models.ForeignKey(DetailCaracteristics, on_delete=models.CASCADE)
    surface = models.FloatField()

class TypeObject(models.Model):
    class ObjectType(models.TextChoices): #To update
        TOOL = 'TOOL'
    type_object = models.CharField(max_length=100, choices=ObjectType.choices)

class Energy(models.Model):
    class EnergyType(models.TextChoices):
        ELECTRICITY = 'ELECTRICITY'
    energy = models.CharField(max_length=100, choices=EnergyType.choices)

class Object(models.Model):
    name = models.CharField(max_length=200)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    caracteristics = models.ForeignKey(Caracteristics, on_delete=models.CASCADE)
    collectiveActors = models.ManyToManyField(CollectiveActor)
    actor = models.ManyToManyField(Actor)
    abstract_object = models.ManyToManyField(AbstractObject)
    definition = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    type_object = models.ForeignKey(TypeObject, on_delete=models.CASCADE)
    energy = models.ForeignKey(Energy, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
