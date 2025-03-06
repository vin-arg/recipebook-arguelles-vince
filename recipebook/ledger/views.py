from django.shortcuts import render
from .models import Recipe

def recipes(request):
    recipes_list = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes_list})

def recipe_ingredients(request, num):
    recipe = Recipe.objects.filter(id=num).first()
    ingredients = recipe.ingredients.all() if recipe else []
    return render(request, 'recipe_ingredients.html', {'recipe': recipe, 'ingredients': ingredients})