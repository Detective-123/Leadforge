from django.db import models
import uuid


# Create your models here
class Company(models.Model):
    title = models.CharField(max_length=150)
    domain = models.CharField(max_length=100, unique=True, db_index=True)
    code = models.CharField(max_length=12, unique=True, blank=True, db_index=True)
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.code:
            while True: 
                new_code = uuid.uuid4().hex[:8].upper()
                if not Company.objects.filter(code=new_code).exists():
                    self.code = new_code
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

