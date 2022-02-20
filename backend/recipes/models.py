from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=255)
    praparation_time = models.PositiveIntegerField(default=0)
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.PositiveIntegerField(default=1)
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
