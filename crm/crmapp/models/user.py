from django.db import models
from django.contrib.auth.models import User

from crm.crmapp.models.common import Company

class Userprofile(models.Model):
    index=models.IntegerField()
    avatar=models.URLField()
    fullname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    gender=models.CharField(max_length=20)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    is_emailverified=models.BooleanField(default=True)
    
    def __str__(self):
        return self.username