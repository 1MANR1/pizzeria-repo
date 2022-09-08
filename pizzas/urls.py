"""Defines URL pattern for pizzas."""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all the available pizzas
    path('pizzas/', views.pizzas, name='pizzas'),
    # Show all the toppings for each pizza
    path('pizzas/<int:pizza_id>/', views.topping, name='topping'),
]