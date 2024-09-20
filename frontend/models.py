from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    feedback = models.CharField(max_length=255, null=True, blank=True)

class Testimonial(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    profession = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    feedback = models.CharField(max_length=255, null=True, blank=True)
    
class Career_Applications(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    whatsapp = models.IntegerField(null=True, blank=True)
    qualification = models.CharField(max_length=255, null=True, blank=True)
    university = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    experience = models.CharField(max_length=255, null=True, blank=True)
    ready_to_relocate = models.BooleanField(null=True, blank=True)
    resume = models.FileField(upload_to='resumes', null=True, blank=True)
    job_applied = models.CharField(max_length=255, null=True, blank=True)