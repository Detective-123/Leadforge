from django.db import models
from django.contrib.auth.models import User

from .common import Company

class Lead(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE, db_index=True)
    owner=models.ForeignKey(User,on_delete=models.SET_NULL)

    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    email=models.EmailField(unique=True, db_index=True)
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
        default="new",
        db_index=True
    )
    value = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    note=models.TextField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["company", "email"],
                name="unique_lead_email_per_company"
            )
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return self.name