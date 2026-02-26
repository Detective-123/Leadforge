from django.db import models
from django.contrib.auth.models import User

from .common import Company

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
    created_at = models.DateTimeField(auto_now_add=True)