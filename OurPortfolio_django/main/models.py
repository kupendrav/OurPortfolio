from django.db import models

# Create your models here.
class Portfolio(models.Model):
  
  # Properties
  name = models.CharField(max_length=100)
  jobTitle = models.CharField(max_length=50)
  shortDescription = models.CharField(max_length=300)
  linkedIn = models.URLField(null=True)
  github = models.URLField(null=True)
  mail = models.EmailField()
  aboutMe = models.CharField(max_length=5000, null=True)
  skills = models.CharField(max_length=300, null=True)


  # Methods
  def __str__(self):
    return self.name