from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import CASCADE


class Unit(models.Model):
    name = models.CharField(max_length=64, unique=True, db_index=True)
    abbreviation = models.CharField(max_length=32)
    physical_quantity = models.CharField(max_length=32)
    si_scale_factor = models.FloatField(validators=[MinValueValidator(0.0)])


class Ingredient(models.Model):
    name = models.CharField(max_length=128, unique=True, db_index=True)
    type = models.CharField(max_length=64)


class Conversion(models.Model):
    unit_1 = models.ForeignKey('Unit', on_delete=CASCADE, related_name='unit_1')
    unit_2 = models.ForeignKey('Unit', on_delete=CASCADE, related_name='unit_2')
    ingredient = models.ForeignKey('Ingredient', on_delete=CASCADE, related_name='conversion')
    unit_1_to_unit_2_factor = models.FloatField(validators=[MinValueValidator(0.0)])


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=CASCADE)
    amount = models.FloatField(validators=[MinValueValidator(0.0)])
    unit = models.FloatField('Unit')


class Category(models.Model):
    name = models.CharField(max_length=64, primary_key=True)


class Recipe(models.Model):
    name = models.CharField(max_length=128)
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes', through='RecipeIngredient')
    steps = ArrayField(models.CharField(max_length=512))
    categories = models.ManyToManyField('Category', related_name='recipes')
    servings = models.IntegerField(validators=[MinValueValidator(0)])
    servings_text = models.CharField(max_length=64)

