from django.db import models

# Create your models here.
class Portfolio(models.Model):
  
  # Properties
  user_name = models.CharField(max_length=100, unique=True, null=True)
  name = models.CharField(max_length=100)
  jobTitle = models.CharField(max_length=50)
  shortDescription = models.CharField(max_length=300)
  profilePic = models.ImageField(upload_to="images", null=True)
  # linkedIn = models.URLField(null=True)
  # github = models.URLField(null=True)
  # mail = models.EmailField(null=True)
  # aboutMe = models.CharField(max_length=5000, null=True)
  # skills = models.CharField(max_length=300, null=True)
  # profile pic

  # Methods
  def __str__(self):
    return self.user_name