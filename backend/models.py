from django.db import models

class Ground(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    capacity = models.CharField(max_length=255, null=True, blank=True)
    rate = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    suite = models.CharField(max_length=255, null=True, blank=True)
    locality = models.CharField(max_length=255, null=True, blank=True)
    agent = models.CharField(max_length=255, null=True, blank=True)
    booking = models.CharField(max_length=255, null=True, blank=True)
    web_link = models.CharField(max_length=255, null=True, blank=True)
    map_link = models.CharField(max_length=255, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    image_1 = models.ImageField(upload_to='stadium', null=True, blank=True)
    image_2 = models.ImageField(upload_to='stadium', null=True, blank=True)
    
class Agent(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    applicant = models.CharField(max_length=255, null=True, blank=True)

class Career(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    experience = models.CharField(max_length=255, null=True, blank=True)
    posted_date = models.CharField(max_length=255, null=True, blank=True)
    closing_date = models.CharField(max_length=255, null=True, blank=True)
    salary = models.CharField(max_length=255, null=True, blank=True)
    place = models.CharField(max_length=255, null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Partners(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='partners', null=True, blank=True)   
    