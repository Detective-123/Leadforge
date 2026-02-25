from django.db import models


# Create your models here.

class Location(models.Model):
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.country} - {self.address}"


class Company(models.Model):
    title = models.CharField(max_length=150)
    domain = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
