from django.http import HttpResponse
from rest_framework import generics

from mat.models import Unit, Ingredient, Recipe, Category
from mat.serializers import UnitSerializer, IngredientSerializer, RecipeSerializer, CategorySerializer


def index(request):
    return HttpResponse('its working')


class UnitView(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class IngredientView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipeView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
