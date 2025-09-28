from django.urls import path
from .views import *
 
urlpatterns = [
    path('pomodoro_timer', pomodoro_timer, name='pomodoro_timer')
]