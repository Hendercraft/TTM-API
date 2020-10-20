from django.db import models

# Create your models here.
"""
Implementation of relationnal models define in static files of the API

To do:
    -check link (foreign key)
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

"""
Quality table
"""

class Quality(models.Model):
    name = models.CharField(max_length=200)
    definition = models.CharField(max_length=200)

"""
Sources & associates tables
"""
class Types(models.Model):
    class type_choice(models.TextChoices):
        SCAN = 'SCAN'
        DDD_MODELS = '3D MODEL'
        
    types_source = models.CharField(max_length=10,choices=type_choice.choices)

class Author(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    status = models.CharField(max_length=200) #To upgrade
    organisation = models.CharField(max_length=200) #To upgrade

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

class Place_Location(models.Model):
    street_number = models.IntegerField()
    street_type = models.CharField(max_length=3)
    street_name = models.CharField(max_length=200) #To update
    city = models.CharField(max_length=100)
    post_code = models.IntegerField()
    country = models.CharField(max_length=100)
    lieu_dit = models.CharField(max_length=200)

class Place_Type(models.Model):
    class Type_Place(models.TextChoices):
        BUILDING = 'BUILDING'
    place_type = models.CharField(max_length=10,choices=Type_Place.choices)

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500) #To update
    place_location = models.ForeignKey(Place_Location, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    place_type = models.ForeignKey(Place_Type, on_delete=models.CASCADE) 

"""
Profession table
"""

class Profession(models.Model):
    name = models.CharField(max_length=200)
    definition = models.CharField(max_length=500)
    autonomous = models.BooleanField(default=False)
    #abstract_objects = models.ManyToManyField(Abstract_Objects)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
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


"""
Actor & associate class
"""


class Actor(models.Model):
    sexe = models.BooleanField()
    profession = models.ManyToManyField(Profession)
    social = models.ForeignKey(Social, on_delete=models.CASCADE)
    #collective_actors = models.ForeignKey(Collective_Actors, on_delete=models.CASCADE)
    #quality = models.ForeignKey(Quality, on_delete=models.CASCADE)
    #social_link = models.ForeignKey(Link, on_delete=models.CASCADE)
    place = models.ManyToManyField(Place)
    source = models.ManyToManyField(Source)

#    def __str__(self):  Return id of the actor
#        return self.

class name_actor(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


"""
Object and associate tables
"""

class Caracteristics(models.Model):
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    state = models.CharField(max_length=500)#To update
    color = models.CharField(max_length=100)#To update
    material = models.CharField(max_length=200)#To update

class Object(models.Model):
    name = models.CharField(max_length=200)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    caracteristics = models.ForeignKey(Caracteristics, on_delete=models.CASCADE)
    #collective_actors = models.ManyToManyField(Collective_Actor)
    actor = models.ManyToManyField(Actor)
    #abstract_object = models.ManyToManyField(Abstract_Object)
    definition = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)