from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class Customer(models.Model):
#     username = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200)

#     def __str__(self):
#          return self.name

class Person(models.Model):
    customer = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50 ,null=True)
    level = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=150, null=True)
    website = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="media/",null=True, blank=True)

    def __str__(self):  
        return self.name if self.name else ''

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    


class Education(models.Model):
    customer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    year = models.CharField(max_length=100)
    qualification = models.TextField(max_length=250)
    universityname = models.CharField(max_length=100)

    def  __str__(self):
        return self.year if self.year else ''
    
class Language(models.Model):
    customer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    language = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=7, decimal_places=0, null=True)

    def __str__(self):
        return self.language if self.language else ''
    

class Profile(models.Model):
    customer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    about = models.CharField(max_length=255)

    def __str__(self):
        return self.about if self.about else ''
    
class Experience(models.Model):
    customer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    year_company = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    about_job = models.TextField(max_length=255)

    def __str__(self):
        return self.year_company if self.year_company else ''
    

class Skills(models.Model):
    customer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    skill = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=7, decimal_places=0, null=True)

    def __str__(self):
        return self.skill if self.skill else ''
    

class Interest(models.Model):
    customer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    interests = models.CharField(max_length=20)
        
    def __str__(self):
        return self.interests if self.interests else ''

