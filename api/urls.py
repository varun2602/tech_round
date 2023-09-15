from django.urls import path 
from . import views 

urlpatterns = [
    path("cuisines", views.CuisineLC_API.as_view()),
    path("cuisinerud/<int:pk>", views.CuisineRetrieveUpdateDestroyAPIView.as_view())
]
