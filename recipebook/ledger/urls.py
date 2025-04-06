from django.urls import path
from .views import recipes, recipe_ingredients, recipe_add

urlpatterns = [
    path('recipes/list/', recipes, name="recipes"),
    path('recipe/<int:num>/', recipe_ingredients, name="recipe_ingredients"), 
    path('recipes/add/', recipe_add, name="recipe_add"),  
]