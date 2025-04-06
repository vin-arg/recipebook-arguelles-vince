from django.urls import path
from .views import recipes, recipe_ingredients, recipe_add, recipe_add_image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('recipes/list/', recipes, name="recipes"),
    path('recipe/<int:num>/', recipe_ingredients, name="recipe_ingredients"), 
    path('recipes/add/', recipe_add, name="recipe_add"),
    path('recipe/<int:num>/add_image', recipe_add_image, name='recipe_add_image')  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)