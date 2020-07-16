from django.shortcuts import render
import datetime

def home(request):
    name = 'David'
    date = datetime.datetime.now().date()
    _context = {
        'name' : name,
        'date' : date
    }
    return render(request, 'home.html', _context)