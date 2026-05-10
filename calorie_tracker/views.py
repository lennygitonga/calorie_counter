from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from .models import FoodItem
import os
import json
from groq import Groq
from django.http import JsonResponse


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

def lookup_calories(request):
    """Use Groq AI to estimate calories for a given food item."""
    if request.method == 'POST':
        data = json.loads(request.body)
        food_name = data.get('food_name', '')
        serving_size = data.get('serving_size', '1 serving')

        client = Groq(api_key=os.environ.get('GROQ_API_KEY'))

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a nutrition expert. When given a food name and serving size, respond with only a JSON object in this exact format with no extra text: {\"calories\": 250, \"note\": \"Approximate calories for the serving size given\"}"
                },
                {
                    "role": "user",
                    "content": f"Food: {food_name}, Serving size: {serving_size}"
                }
            ],
            model="llama3-8b-8192",
        )

        response_text = chat_completion.choices[0].message.content
        result = json.loads(response_text)
        return JsonResponse(result)

    return JsonResponse({'error': 'Invalid request'}, status=400)