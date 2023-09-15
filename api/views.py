from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import models
from . import serializers



class CuisineLC_API(ListCreateAPIView):
    queryset = models.Cuisines.objects.all()
    serializer_class = serializers.CuisineSerializer
    

class CuisineRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Cuisines.objects.all()
    serializer_class = serializers.CuisineSerializer
    
