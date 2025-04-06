from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.decorators import login_required
from .forms import RecipeIngredientForm


def recipes(request):
    recipes_list = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes_list})

@login_required
def recipe_ingredients(request, num):
    recipe = Recipe.objects.filter(id=num).first()
    ingredients = recipe.ingredients.all() if recipe else []
    author_name = recipe.author.username if recipe else "Unknown"

    if (request.method == "POST"):
        form  = RecipeIngredientForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('recipe_ingredients', num = num)

    form = RecipeIngredientForm()

    return render(request, 'recipe_ingredients.html', {'recipe': recipe, 'ingredients': ingredients, 'author_name': author_name, 'ingredients_form':form},)