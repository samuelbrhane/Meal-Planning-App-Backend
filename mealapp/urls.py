from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import meals_list, meal_detail, user_meals

urlpatterns = [
    path('', meals_list, name="meals-list"),
    path('<int:id>/', meal_detail, name="meal-detail"),
    path('user/<int:user_id>/', user_meals, name="user-meals"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
