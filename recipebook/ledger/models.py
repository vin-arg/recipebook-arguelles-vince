from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    Bio = models.CharField(max_length=255)


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.id)])

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=now)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_ingredients', args=[str(self.id)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=200)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
