from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Direction, Succursale, Client, Assurance

admin.site.register(Direction)
admin.site.register(Succursale)
admin.site.register(Client)
admin.site.register(Assurance)
