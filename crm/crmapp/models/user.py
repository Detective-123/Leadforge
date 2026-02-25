from django.db import models
from django.contrib.auth.models import User

from .common import Company

class Userprofile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    avatar=models.URLField()
    fullname=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    is_emailverified=models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username
    

# REMOVED FIELDS
# username=models.CharField(max_length=100)
# email=models.EmailField(unique=True)
# is_active=models.BooleanField(default=True)