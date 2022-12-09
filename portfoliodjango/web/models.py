from django.db import models
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to="services/")
class Email(models.Model):
    email = models.EmailField()
    isMain = models.BooleanField()
class Telephone(models.Model):
    codeCountry = models.CharField(max_length=3)
    phone = models.CharField(max_length=9)
    isMain = models.BooleanField()
class Customer(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
    img = models.ImageField(upload_to="customer/")
class Colleague(models.Model):
    name =models.CharField(max_length=50)
    link = models.URLField()
    img = models.ImageField(upload_to="colleague/")
class Project(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="projects/")
class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
class Location(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
class Language(models.Model):
    language = models.CharField(max_length=50)
class Education(models.Model):
    company = models.CharField(max_length=100)
    topic = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField(upload_to="education/")
class DetailSkill(models.Model):
    name = models.CharField(max_length=100)
class Skill(models.Model):
    name = models.CharField(max_length=100)
    details = models.ManyToManyField(DetailSkill)
class Person(models.Model):
    dni = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    img = models.ImageField(upload_to="person/")
    description = models.TextField()
    skills = models.ManyToManyField(Skill)
    educations = models.ManyToManyField(Education)
    Languages = models.ManyToManyField(Language)
    Locations = models.ManyToManyField(Location)
    SocialMedia = models.ManyToManyField(SocialMedia)
    projects = models.ManyToManyField(Project)
    colleagues = models.ManyToManyField(Colleague)
    Customers = models.ManyToManyField(Customer)
    telephones = models.ManyToManyField(Telephone)
    emails = models.ManyToManyField(Email)
    services = models.ManyToManyField(Service)
