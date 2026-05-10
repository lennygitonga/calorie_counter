from django.db import models


class FoodItem(models.Model):
    """Represents a single food item and its calorie count."""

    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    name = models.CharField(max_length=200)
    calories = models.PositiveIntegerField()
    serving_size = models.CharField(max_length=100)
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES, default='snack')
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.calories} calories"