from django.contrib import admin
from .models import Comments 

# Register your models here.

admin.site.register(Comments)  # Assuming Comment model exists in comments/models.py