from django.contrib import admin

from .models import Portfolio, Qualification , Skill

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Qualification)
admin.site.register(Skill)

