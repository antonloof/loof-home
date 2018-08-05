from django.db import models
from django.contrib.postgres.fields import ArrayField


class Unit(models.Model):
    name = models.CharField(max_length=64)
    abbreviation = models.CharField(max_length=32)
    physical_quantity = models.CharField(max_length=32)
    si_scale_factor = models.FloatField(min=0)


class Ingredient(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=64)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe')
    ingredient = models.ForeignKey('Ingredient')
    amount = models.FloatField(min=0)
    unit = models.ForeignKey('Unit')


class Recipe(models.Model):
    name = models.CharField(max_length=128)
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes', through='RecipeIngredient')
    steps = ArrayField(models.CharField(max_length=512))
    types = ArrayField(models.CharField(max_length=64))
    servings = models.IntegerField(min=0)
    servings_text = models.CharField(max_length=64)

