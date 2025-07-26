from django.contrib import admin
from .models import  Recipe



class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'category', 'date_added')

admin.site.register(Recipe, RecipeAdmin)
