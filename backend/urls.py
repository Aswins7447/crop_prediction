from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('get_sensor_data', views.get_sensor_data)
]