from django.db import models



# Create your models here.
class Portfolio(models.Model):
  # Template choosing for displaying
  THEMES = [
    ("BLUE", "Blue Theme"),
    ("CREAM", "Elegent Cream"),
    ("DEFAULT", "Default Theme"),
    ("DARK", "Dark Woods")
  ]

  
  # Properties
  user_name = models.CharField(max_length=100, unique=True, null=True)
  # Use first name and last
  name = models.CharField(max_length=100)

  # ? Ask for alternative or better name for jobtitle
  jobTitle = models.CharField(max_length=50)
  shortDescription = models.CharField(max_length=300)
  
# Keeps im
  profilePic = models.ImageField(upload_to="images", null=True)
  porfolioTemplate = models.CharField(max_length=10, choices=THEMES, default="DEFAULT")

  # SOCIALS

  # twitter = 
  # linkedIn = models.URLField(null=True)
  # github = models.URLField(null=True)
  # mail = models.EmailField(null=True)
  # insta
  
  # aboutMe = models.CharField(max_length=5000, null=True)
  # skills = models.CharField(max_length=300, null=True)
    # what level of expertise 
  # contact me
  # shareMy profile

  # Methods
  def __str__(self):
    return self.user_name
  

# Good but not neccesary
# 1. Hire me
# 2. Showcase their work / projects
# *3. Certification
# 4. Services offered
# 5. Testimonials
# 6. Download as pdf
# *7. RESUME/CV LINK