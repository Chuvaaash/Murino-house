from django.contrib import admin
from .models import Occupant
from .models import Hobby

# Register your models here.
admin.site.register(Occupant)
admin.site.register(Hobby)
