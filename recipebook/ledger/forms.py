from django import forms
from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'author']

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = '__all__'
