from django.contrib import admin

# Register your models here.
from .models import Researchpaper,  People

admin.site.register(Researchpaper)
admin.site.register(People)
