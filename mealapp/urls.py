from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import meals_list, meal_detail, user_meals,meal_by_date

urlpatterns = [
    path('', meals_list, name="meals-list"),
    path('<int:id>/', meal_detail, name="meal-detail"),
    path('user/<int:user_id>/', user_meals, name="user-meals"),
    path('date/<str:selected_date>/', meal_by_date, name="date-meals"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
