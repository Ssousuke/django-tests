from django.test import TestCase
from django.urls import reverse


class RecipeUrlsTests(TestCase):
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recipe_category_url_is_correct(self):
        category_url = reverse('recipes:category', kwargs={'id': 1})
        self.assertEqual(category_url, '/receita/categoria/1/')

    def test_recipe_detail_url_is_correct(self):
        recipe_detail = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(recipe_detail, '/receita/detalhe/1/')
