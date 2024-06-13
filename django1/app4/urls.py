from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_permutations, name='calculate_permutations'),
]
