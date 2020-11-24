from django.db import models

# Create your models here.

# User add on model

class UserInformation(models.Model):
    postalAdress = models.IntegerField(null=True, blank=True)
    phoneNumber = models.IntegerField(null=True, blank=True)
    profileImage = models.URLField(null=True, blank=True)

    #If the user had worked on the site
    workedOnTheSite = models.BooleanField(default=False)
    workedInCompany = models.CharField(max_length=255, null=True, blank=True)
    workTimeDuration = models.IntegerField(null=True, blank=True) # Number of years




# Discipline model
class Discipline (models.Model):
    discipline = models.CharField(max_length=255, null=True, blank=True)
    commentsDiscipline = models.CharField(max_length=255, null=True, blank=True)

# Research fields model
class ResearchField(models.Model):
    researchField = models.CharField(max_length=255, null=True, blank=True)
    commentsResearch = models.CharField(max_length=255, null=True, blank=True)

# Research establishment model
class ResearchEstablishment(models.Model):
    laboratory = models.CharField(max_length=255, null=True, blank=True)
    establishment = models.CharField(max_length=255, null=True, blank=True)
    commentsEstablishment = models.CharField(max_length=255, null=True, blank=True)