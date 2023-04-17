from django.urls import path
from . import views

urlpatterns = [
    # Routes for CRUD operations on meals
    path('', views.meal_list, name='meal_list'),
    path('detail/<str:pk>/', views.meal_detail, name='meal_detail'),
    
    # Route to get all food items for a single person
    path('user/<str:pk>/', views.getMealsByUserId, name='get_meals_by_userId'),
]
