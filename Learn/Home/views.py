from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import time
def HomeView(request):

    student = [
        "gaurva",
        "Ayush",
        {'name': 'abhimanyu'},
        {'name': 'abhimanyu'},
        {'name': 'abhimanyu'},
        "jack",
        "sororz",
        "abhimanyu",
        "chipanji",
    ]
    
    return render(request, 'home.html', context={'students':student})
