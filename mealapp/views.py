from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Meal
from .serializers import MealSerializer

# Get all meals for all users or create a new meal
@csrf_exempt
@api_view(['GET', 'POST'])
def meals_list(request):
    # get all meals   
    if request.method == 'GET':       
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    # create a new meal
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['user'] = request.user.id       
        try:
            meal = Meal.objects.get(user=request.user, selectedDate=data['selectedDate'])
            serializer = MealSerializer(meal)
            return JsonResponse({'error': f"Meal already created for {data['selectedDate']}"})
        except Meal.DoesNotExist:
            pass

        serializer = MealSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# Get, update or delete a single meal
@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def meal_detail(request, id):
    try:
        meal = Meal.objects.get(id=id)
    except Meal.DoesNotExist:
        return JsonResponse({'message': 'The meal does not exist'}, status=404)

    if meal.user != request.user:
        return JsonResponse({'message': 'Unauthorized'}, status=401)

# get single meal by id
    if request.method == 'GET':
        serializer = MealSerializer(meal)
        return JsonResponse(serializer.data)

# update a meal 
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MealSerializer(meal, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

# delete a meal
    elif request.method == 'DELETE':
        meal.delete()
        return JsonResponse({'message': 'Meal was deleted successfully!'}, status=204)

# Get all meals for a single user
@csrf_exempt
@api_view(['GET'])
def user_meals(request, user_id):
    if request.user.id != user_id:
        return JsonResponse({'message': 'Unauthorized'}, status=401)

    meals = Meal.objects.filter(user=user_id)
    serializer = MealSerializer(meals, many=True)
    return JsonResponse(serializer.data, safe=False)

# Get single meal based on selectedDate
@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def meal_by_date(request, selected_date):
    try:
        meal = Meal.objects.get(user=request.user, selectedDate=selected_date)
    except Meal.DoesNotExist:
        return JsonResponse({'message': 'The meal does not exist'}, status=404)

    serializer = MealSerializer(meal)
    return JsonResponse(serializer.data)

