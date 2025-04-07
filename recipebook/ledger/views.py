from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, RecipeIngredientForm, IngredientForm, RecipeImageForm


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

@login_required
def recipe_add(request):
    
    if (request.method == "POST"):
        form = RecipeForm(request.POST)
        ingredient_form = IngredientForm(request.POST)
        recipe_ingredient_form = RecipeIngredientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('recipes')
        elif ingredient_form.is_valid():
            ingredient_form.save()
            return redirect('recipe_add')
        elif recipe_ingredient_form.is_valid():
            recipe_ingredient_form.save()
            return redirect('recipe_add')

    
    form = RecipeForm()
    ingredient_form = IngredientForm()
    recipe_ingredient_form = RecipeIngredientForm()

    return render(request, 'recipe_add.html', {'recipe_form':form, 'ingredient_form': ingredient_form, 'recipe_ingredient_form': recipe_ingredient_form},)

@login_required
def recipe_add_image(request, num):
    
    if (request.method == "POST"):
        form = RecipeImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        return redirect('recipe_ingredients', num = num)
    
    form = RecipeImageForm()

    return render(request, 'recipe_add_image.html', {'image_form':form},)