from rest_framework.serializers import ModelSerializer

import mat.models as models


class UnitSerializer(ModelSerializer):
    class Meta:
        model = models.Unit
        fields = '__all__'


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = '__all__'


class RecipeIngredientSerializer(ModelSerializer):
    class Meta:
        model = models.RecipeIngredient
        fields = '__all__'


class RecipeSerializer(ModelSerializer):
    class Meta:
        model = models.Recipe
        fields = '__all__'


class ConversionSerializer(ModelSerializer):
    class Meta:
        model = models.Conversion
        fields = '__all__'


class RecipeIngredientSerializer(ModelSerializer):
    class Meta:
        model = models.RecipeIngredient
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
