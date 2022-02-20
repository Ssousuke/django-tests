from django.urls import path
from .import views

app_name = 'recipes'
urlpatterns = [
    path('', views.home, name='home'),
    path('receita/detalhe/<int:id>/', views.recipe, name='recipe'),
    path('receita/categoria/<int:id>/', views.category, name='category'),
]
