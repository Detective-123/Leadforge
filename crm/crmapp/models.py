from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    country=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.country} - {self.address}"

class Company(models.Model):
    title=models.CharField(max_length=150)
    domain=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    title=models.CharField(max_length=100)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    domain=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


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

class Lead(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    email=models.EmailField(unique=True)
    source=models.CharField(max_length=100)
    STATUS_CHOICE=[
        ('new','New'),
        ('contacted','Contacted'),
        ('qualified','Qualified'),
        ('converted','Converted'),
        ('lost','Lost')
    ]
    status=models.CharField(
        max_length=20,
        choices=STATUS_CHOICE,
        default="new"
        
    )
    value = models.DecimalField(max_digits=12, decimal_places=2)
    note=models.TextField(blank=True)
    def __str__(self):
        return self.name
class Task(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    assignedTo=models.ForeignKey(User,on_delete=models.CASCADE,related_name="tasks_assigned")
    assignedBy=models.ForeignKey(User,on_delete=models.CASCADE,related_name="tasks_created")
    model_choice=[
        ('lead','Lead'),
        ('contact','Contact'),
        ('deal','Deal'),
    ]
    related_models=models.CharField(
        max_length=20,
        choices=model_choice,
    )
    STATUS_CHOICE=[
        ('pending','Pending'),
        ('in-progress','In-progress'),
        ('completed','Completed')
    ]
    status=models.CharField(
        max_length=20,
        choices=STATUS_CHOICE,
        default='pending'
    )
    duedate=models.DateField()
    attachement=models.URLField()
    description=models.CharField(max_length=200)

class Deal(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    contact=models.ForeignKey(Contact,on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    STAGE_CHOICE=[
        ('prospecting','Prospecting'),
        ('qualification','Qualification'),
        ('proposal','Proposal'),
        ('negotiation','Negotiation'),
        ('closed-won','Closed-won'),
        ('closed-lost','Closed-lost')
    ]
    stage=models.CharField(
        max_length=20,
        choices=STAGE_CHOICE,
        default="prospecting"
    )
    expected_closed_date=models.DateField()
    note=models.TextField(blank=True)
    