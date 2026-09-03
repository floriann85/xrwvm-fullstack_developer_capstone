from django.contrib import admin
from .models import CarMake, CarModel

# Inline class to show CarModels inside CarMake
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # number of empty rows shown

# Admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'year', 'dealer_id', 'car_make')
    list_filter = ('type', 'year', 'car_make')
    search_fields = ('name',)

# Admin class for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    inlines = [CarModelInline]

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)