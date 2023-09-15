from rest_framework import serializers 
from . import models

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cuisines 
        fields = ["id","cuisine_name"]

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant 
        fields = ["id", "restaurant_name", "number_of_tables", "cuisine"]

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Listings
        fields = ["id", "restaurant"]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cuisines 
        fields = ["id", "customer_name", "restaurant", "datetime", "duration"]
