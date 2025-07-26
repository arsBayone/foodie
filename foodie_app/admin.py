from django.contrib import admin
from foodie_app.models import Category, Recipe


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id",'name', 'date_added')
    search_fields = ['name']

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'category', 'date_added')

admin.site.register(Category, CategoryAdmin)    
admin.site.register(Recipe, RecipeAdmin)
