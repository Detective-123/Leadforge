from django.db import models
from django.contrib.auth.models import User

from .common import Company
from .contact import Contact

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
    created_at = models.DateTimeField(auto_now_add=True)
    note=models.TextField(blank=True)