from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required


def recipes(request):
    recipes_list = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes_list})

@login_required
def recipe_ingredients(request, num):
    recipe = Recipe.objects.filter(id=num).first()
    ingredients = recipe.ingredients.all() if recipe else []
    author_name = recipe.author.username if recipe else "Unknown"
    return render(request, 'recipe_ingredients.html', {'recipe': recipe, 'ingredients': ingredients, 'author_name': author_name})