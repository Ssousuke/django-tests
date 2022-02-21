from django.test import TestCase
from django.urls import resolve, reverse
from .. import views
from ..models import Category, Recipe, User


class RecipeViewsTest(TestCase):
    # Checam se a identidade em memoria das variaveis são iguais
    def test_recipe_home_views_function_is_correct(self):
        view_home = resolve('/')
        self.assertIs(view_home.func, views.home)

    def test_recipe_category_views_function_is_correct(self):
        view_category = resolve(reverse('recipes:category', kwargs={'id': 1}))
        self.assertIs(view_category.func, views.category)

    def test_recipe_detail_views_function_is_correct(self):
        view_detail = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view_detail.func, views.recipe)

    # Checa o status code retornado pelas views
    # Utiliza o Client do django
    # https://docs.djangoproject.com/en/4.0/topics/testing/tools/
    def test_recipe_home_view_returns_status_code_200(self):
        """
        O client simula um navegador web fazendo solicitações.
        Nesse caso ele pode fazer GET e POST
        """
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    # Fixtures
    def test_recipe_home_template_loads_recipe(self):
        category = Category.objects.create(name='Salgados')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@gmail.com',
        )
        recipe = Recipe.objects.create(
            title='Olá Mundo!',
            description='Olá Mundo!',
            preparation_time=2,
            preparation_time_unit='Minutos',
            servings=2,
            servings_unit='Porções',
            preparation_steps='Recipes prepatarion steps',
            preparation_steps_is_html=False,
            is_published=True,
            category=category,
            author=author,
        )
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        self.assertIn('Olá Mundo!', content)

    # Testa se o category retorna 404
    def test_recipe_category_view_returns_status_code_404(self):
        response = self.client.get(reverse('recipes:category', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    # Testa se o detail retorna 404
    def test_recipe_detail_view_returns_status_code_404(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 10000}))
        self.assertEqual(response.status_code, 404)

    # Testa os templates retornado pela home
    def test_recipe_home_view_load_correct_template(self):
        """
        Testa se o template passado é o mesmo que está sendo
        usado na renderização
        """
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'pages/index.html')

    # Testa o html da Home em casos de 404
    def test_recipe_home_template_shows_no_recipe_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1 class="display-1">Ainda não temos nenhuma publicação aqui!</h1>',
            response.content.decode('utf-8')
        )
