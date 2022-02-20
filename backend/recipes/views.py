from django.shortcuts import render
from .models import Recipe, Category


def home(request):
    recipes = Recipe.objects.filter(is_published=True)
    return render(request, 'pages/index.html', {'recipes': recipes})
