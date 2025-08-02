from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("config/", include("config.urls")),
    path("", include("foodie_app.urls")),
    path("recipes/", include("recipes.urls")),
    path("comments/", include("comments.urls"))
]
