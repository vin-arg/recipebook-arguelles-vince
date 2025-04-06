from django.urls import path
from .views import recipes, recipe_ingredients

urlpatterns = [
    path('recipes/list/', recipes, name="recipes"),
    path('recipe/<int:num>/', recipe_ingredients, name="recipe_ingredients") 
      
]