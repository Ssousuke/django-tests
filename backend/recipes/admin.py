from django.contrib import admin
from .models import Category, Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at',
                    'updated_at', 'is_published',)
    list_diplay_links = ('title', 'description', 'created_at',
                         'updated_at',)
    list_editable = ('is_published',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
