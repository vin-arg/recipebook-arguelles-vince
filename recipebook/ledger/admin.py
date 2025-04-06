from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Profile, RecipeImage
from django.contrib.auth.models import User

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)

class RecipeImageInline(admin.StackedInline):
    model = RecipeImage
    extra = 1 

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeImageInline]
    list_display = ('name', 'author', 'created_on', 'updated_on',)

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'ingredient', 'recipe',)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]

class RecipeImageAdmin(admin.ModelAdmin):
    list_display = ['recipe', 'description', 'recipe',]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)
