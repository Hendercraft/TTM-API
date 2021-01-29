from django.db import models
from django.contrib.auth.models import Group, AbstractUser



class UserProfile(AbstractUser):
    postalAdress = models.CharField(max_length=255, null=True, blank=True)
    phoneNumber = models.IntegerField(null=True, blank=True)
    profileImage = models.URLField(null=True, blank=True)
    

    #If the user had worked on the site
    workedOnTheSite = models.BooleanField(default=False)
    workedInCompany = models.CharField(max_length=255, null=True, blank=True)
    workTimeDuration = models.IntegerField(null=True, blank=True) # Number of years
    

    #If the user is a researcher
    disciplineFK = models.ForeignKey("Discipline", on_delete=models.CASCADE, default=None, null=True, blank=True)
    researchFieldFK = models.ForeignKey("ResearchField", on_delete=models.CASCADE, default=None, null=True, blank=True)
    researchEstablishmentFK = models.ForeignKey("ResearchEstablishment", on_delete=models.CASCADE, default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username

# Discipline model
class Discipline (models.Model):
    user = models.ForeignKey(UserProfile, on_delete= models.CASCADE, default=None, null=True, blank=True)
    discipline = models.CharField(max_length=255, null=True, blank=True)
    commentsDiscipline = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.discipline

# Research fields model
class ResearchField(models.Model):
    user = models.ForeignKey(UserProfile, on_delete= models.CASCADE, default=None)
    researchField = models.CharField(max_length=255, null=True, blank=True)
    commentsResearch = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.researchField

# Research establishment model
class ResearchEstablishment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete= models.CASCADE, default=None)
    laboratory = models.CharField(max_length=255, null=True, blank=True)
    establishment = models.CharField(max_length=255, null=True, blank=True)
    commentsEstablishment = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.establishment + " " + self.laboratory
