from django.db import models
from django.contrib.auth.models import User
# User add on model






# Discipline model
class Discipline (models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, default=None)
    discipline = models.CharField(max_length=255, null=True, blank=True)
    commentsDiscipline = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.discipline

# Research fields model
class ResearchField(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, default=None)
    researchField = models.CharField(max_length=255, null=True, blank=True)
    commentsResearch = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.researchField

# Research establishment model
class ResearchEstablishment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, default=None)
    laboratory = models.CharField(max_length=255, null=True, blank=True)
    establishment = models.CharField(max_length=255, null=True, blank=True)
    commentsEstablishment = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.establishment + " " + self.laboratory

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, default=None)
    postalAdress = models.IntegerField(null=True, blank=True)
    phoneNumber = models.IntegerField(null=True, blank=True)
    profileImage = models.URLField(null=True, blank=True)
    

    #If the user had worked on the site
    workedOnTheSite = models.BooleanField(default=False)
    workedInCompany = models.CharField(max_length=255, null=True, blank=True)
    workTimeDuration = models.IntegerField(null=True, blank=True) # Number of years
    

    #If the user is a researcher
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, default=None)
    researchField = models.ForeignKey(ResearchField, on_delete=models.CASCADE, default=None)
    researchEstablishment = models.ForeignKey(ResearchEstablishment, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.username
    