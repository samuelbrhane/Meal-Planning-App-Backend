from django.contrib import admin
from .models import Meal, FoodItem

# Register your models here.
admin.site.register(Meal)
admin.site.register(FoodItem)