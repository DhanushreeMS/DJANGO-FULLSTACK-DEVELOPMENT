from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_student, name='register_student'),
]
