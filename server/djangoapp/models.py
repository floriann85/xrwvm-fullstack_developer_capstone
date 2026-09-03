# Uncomment the following imports before adding the Model code
from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    # Many-to-one relationship
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    # Car type choices
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('COUPE', 'Coupe'),
    ]

    type = models.CharField(max_length=20, choices=CAR_TYPES, default='SUV')

    # Dealer ID (Cloudant dealer)
    dealer_id = models.IntegerField()

    # Year with validators
    year = models.IntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)
        ]
    )

    def __str__(self):
        return f"{self.name} ({self.year})"
