from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe, Category


def home(request):
    recipes = Recipe.objects.filter(is_published=True)
    return render(request, 'pages/index.html', {'recipes': recipes})


def category(request, id):
    category = get_list_or_404(Recipe, is_published=True, category__id=id)
    return render(request, 'pages/category.html', {'category': category})


def recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, is_published=True)
    return render(request, 'pages/recipe.html', {'recipe': recipe})
