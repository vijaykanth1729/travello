from django.urls import path
from .views import travello_home

app_name = "travello"
urlpatterns = [

    path('travello/', travello_home, name='travello-home')
]
