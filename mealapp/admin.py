from django.contrib import admin
from .models import Meal

class MealAdmin(admin.ModelAdmin):
    list_display = ("id", "user","selectedDate","plannedCalories")
    list_display_links = ("id", "user")
    search_fields = ("id","user")
    list_per_page = 25
    
    
admin.site.register(Meal, MealAdmin)
