from django.db import models

from recipes.models import Recipe

# Create your models here.


class Comments(models.Model):
    recipie = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text= models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text