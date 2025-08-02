# recipes/admin.py - CORRECTED VERSION
from django.contrib import admin
from .models import Recipe  # Import from current app's models, not foodie_app

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'category', 'date_added')

admin.site.register(Recipe, RecipeAdmin)