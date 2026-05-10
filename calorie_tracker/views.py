from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from .models import FoodItem


def index(request):
    """Display all food items and the total calories for the day."""
    food_items = FoodItem.objects.filter(date_added=date.today())
    total_calories = sum(item.calories for item in food_items)
    
    context = {
        'food_items': food_items,
        'total_calories': total_calories,
    }
    return render(request, 'calorie_tracker/index.html', context)


def add_food(request):
    """Add a new food item to the database."""
    if request.method == 'POST':
        name = request.POST.get('name')
        calories = request.POST.get('calories')
        FoodItem.objects.create(name=name, calories=calories)
        return redirect('index')
    return redirect('index')


def delete_food(request, food_id):
    """Delete a food item from the database."""
    food_item = get_object_or_404(FoodItem, id=food_id)
    food_item.delete()
    return redirect('index')


def reset_calories(request):
    """Delete all food items added today."""
    FoodItem.objects.filter(date_added=date.today()).delete()
    return redirect('index')