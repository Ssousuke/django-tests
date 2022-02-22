from django.test import TestCase

from backend.recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    @staticmethod
    def make_category():
        return Category.objects.create(name='Salgados')

    @staticmethod
    def make_author():
        return User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@gmail.com',
        )

    def make_recipe(self, category_data=None, author_data=None):
        if category_data is None:
            category_data = {}
        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title='Olá Mundo!',
            description='Olá Mundo, Descrição!',
            slug='ola-mundo',
            preparation_time=2,
            cover='django-test.png',
            preparation_time_unit='Minutos',
            servings=2,
            servings_unit='Porções',
            preparation_steps='Recipes prepatarion steps',
            preparation_steps_is_html=False,
            is_published=True,
        )
