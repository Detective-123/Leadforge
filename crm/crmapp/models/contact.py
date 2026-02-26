from django.db import models
from django.contrib.auth.models import User

from .common import Company


class Contact(models.Model):
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    domain = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
