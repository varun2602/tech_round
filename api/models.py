from django.db import models


class Cuisines(models.Model):
    cuisine_name = models.CharField(max_length = 100, blank = True, null = True)

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length = 100, blank = True, null=True)
    number_of_tables = models.IntegerField()
    cuisine = models.ForeignKey(Cuisines, on_delete= models.CASCADE)

class Listings(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Booking(models.Model):
    customer_name = models.CharField(max_length = 100, blank = True, null = True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    duration = models.IntegerField()

