from django.db import models

from foodie_app.models import Category  # CORRECT
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    ingredient = models.TextField()
    direction = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 

    
    def __str__(self):
        return self.name