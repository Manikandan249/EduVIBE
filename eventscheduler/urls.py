from django.urls import path
from eventscheduler import views

urlpatterns=[
    path('calendar/', views.calendar, name='calendar')
]