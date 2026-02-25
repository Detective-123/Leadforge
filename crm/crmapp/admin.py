from django.contrib import admin
from .models import Userprofile, Company, Contact, Deal, Lead, Task


# Register your models here.
admin.site.register(Userprofile)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Deal)
admin.site.register(Lead)
admin.site.register(Task)