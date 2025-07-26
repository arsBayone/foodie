from django.contrib import admin
from foodie_app.models import  Recipe



class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'category', 'date_added')

admin.site.register(Recipe, RecipeAdmin)
