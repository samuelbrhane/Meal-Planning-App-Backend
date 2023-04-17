from django.db import models
from django.conf import settings

# create food items class
class FoodItem(models.Model):
    uri = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    image = models.URLField()
    healthLabels = models.JSONField()
    ingredientLines = models.JSONField()
    ingredients = models.JSONField()
    calories = models.FloatField()
    nutrients = models.JSONField()

    def __str__(self):
        return self.title


# create a new meal
class Meal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    selectedDate = models.CharField(max_length=8, unique=True)
    breakfast = models.ManyToManyField(FoodItem, related_name='breakfast_set')
    lunch = models.ManyToManyField(FoodItem, related_name='lunch_set')
    snack = models.ManyToManyField(FoodItem, related_name='snack_set')
    dinner = models.ManyToManyField(FoodItem, related_name='dinner_set')

    def __str__(self):
        return f"{self.user}'s meal on {self.selectedDate}"
