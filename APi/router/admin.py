from django.contrib import admin

# Register your models here.

from .models import Router


#class Router(admin.ModelAdmin):
#    list_display = ('FirstName','Profession','DigitalAddress','ResidentialStatus','DateTime')

admin.site.register(Router)


