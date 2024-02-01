from django.shortcuts import render
from datetime import datetime

# Create your views here.


def get_time_greeting():
    current_time = datetime.now().time()

    if current_time < datetime.strptime("12:00:00", "%H:%M:%S").time():
        greeting = "Good Morning."
    elif current_time < datetime.strptime("18:00:00", "%H:%M:%S").time():
        greeting = "Good Afternoon."
    else:
        greeting = "Good Night."

    return greeting


def greeting_view(request):
    user_greeting = get_time_greeting()
    return render(request,'view.html', {'user_greeting': user_greeting})
