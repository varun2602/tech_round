from django.contrib import admin
from . import models 

@admin.register(models.Listings)
class ListingAdmin(admin.ModelAdmin):
    list_display = ["id", "restaurant"]

@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ["id", "customer_name", "restaurant", "datetime", "duration"]

@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["id", "restaurant_name"]
    
@admin.register(models.Cuisines)
class CuisineAdmin(admin.ModelAdmin):
    list_display = ["id", "cuisine_name"]


