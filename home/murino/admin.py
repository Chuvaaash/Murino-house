from django.contrib import admin
from .models import Occupant
from .models import Hobby
from .models import KissTransaction

# Register your models here.
admin.site.register(Occupant)
admin.site.register(Hobby)
admin.site.register(KissTransaction)
