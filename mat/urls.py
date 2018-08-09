from django.urls import path

import mat.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('unit', views.UnitView.as_view(), name='unit_list'),
    path('recipe', views.RecipeView.as_view(), name='recipe_list'),
    path('ingredient', views.IngredientView.as_view(), name='ingredient_list'),
    path('category', views.CategoryView.as_view(), name='category_list'),
]
