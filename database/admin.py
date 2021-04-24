from django.contrib import admin
from .models import *
# Register your models here.

#Modify table
admin.site.register(ModifyAttribute)

#Source tables
admin.site.register(Source)
# admin.site.register(SourceType)
admin.site.register(Author)
admin.site.register(Content)
admin.site.register(Files)

#Date table
admin.site.register(Date)

#Quality table
admin.site.register(Quality)

#Place tables
admin.site.register(Place)
admin.site.register(PlaceType)
admin.site.register(PlaceLocation)

#Knowledge table
admin.site.register(Knowledge)

#Collective actor table
admin.site.register(CollectiveActor)

#Abstract object table
admin.site.register(AbstractObject)

#Profession table
admin.site.register(Profession)

#Social tables
admin.site.register(SocialActivity)
admin.site.register(SocialLink)

#Actor tables
admin.site.register(Actor)
admin.site.register(NameActor)

#Object tables
admin.site.register(Building)
admin.site.register(Object)
admin.site.register(TypeObject)
admin.site.register(Energy)
admin.site.register(Caracteristic)
admin.site.register(DetailCaracteristic)