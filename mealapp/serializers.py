from rest_framework.serializers import ModelSerializer
from .models import Meal, FoodItem

class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"
        
class FoodItemSerializer(ModelSerializer):
    class Meta:
        model = FoodItem
        fields: "__all__"