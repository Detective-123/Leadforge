from django.db import models
from django.contrib.auth.models import User

from .common import Company, Location

class Contact(models.Model):
    title=models.CharField(max_length=100)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    domain=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title