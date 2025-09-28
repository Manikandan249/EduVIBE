from django.shortcuts import render, redirect


 
# views.py
 
def pomodoro_timer(request):
    return render(request, "pomodoro_timer.html")

