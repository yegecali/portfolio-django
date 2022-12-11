from django.db import models
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to="services/")
    def __str__(self):
        return self.name
class Email(models.Model):
    email = models.EmailField()
    isMain = models.BooleanField()
    def __str__(self):
        return self.email
class Telephone(models.Model):
    codeCountry = models.CharField(max_length=3)
    phone = models.CharField(max_length=9)
    isMain = models.BooleanField()
    def __str__(self):
        return self.phone
class Customer(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
    img = models.ImageField(upload_to="customer/")
    def __str__(self):
        return self.name
class Colleague(models.Model):
    name =models.CharField(max_length=50)
    link = models.URLField()
    img = models.ImageField(upload_to="colleague/")
    def __str__(self):
        return self.name
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField(upload_to="projects/")
    def __str__(self):
        return self.name
class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name
class Location(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    def __str__(self):
        return "%s %s" % (self.country, self.city)
class Language(models.Model):
    language = models.CharField(max_length=50)
    def __str__(self):
        return self.language
class Education(models.Model):
    company = models.CharField(max_length=100)
    topic = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField(upload_to="education/")
    def __str__(self):
        return "%s - %s" % (self.company, self.topic)
class DetailSkill(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="details/")
    def __str__(self):
        return self.name
class Skill(models.Model):
    name = models.CharField(max_length=100)
    details = models.ManyToManyField(DetailSkill)
    def __str__(self):
        return self.name
class Person(models.Model):
    dni = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    img = models.ImageField(upload_to="person/")
    description = models.TextField()
    skills = models.ManyToManyField(Skill)
    educations = models.ManyToManyField(Education)
    languages = models.ManyToManyField(Language)
    locations = models.ManyToManyField(Location)
    socialMedias = models.ManyToManyField(SocialMedia)
    projects = models.ManyToManyField(Project)
    colleagues = models.ManyToManyField(Colleague)
    customers = models.ManyToManyField(Customer)
    telephones = models.ManyToManyField(Telephone)
    emails = models.ManyToManyField(Email)
    services = models.ManyToManyField(Service)
    def __str__(self):
        return self.name
