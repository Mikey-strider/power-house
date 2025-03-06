from django.http import HttpResponse
from django.shortcuts import render

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def current(request):
    return render(request, 'current.html', {'current' : current})

def staff(request):
    return render(request, 'staff-past.html', {'staff-past' : staff-past})

def history(request):
    return render(request, 'bar-history.html', {'bar-history' : bar-history})

def contact(request):
    return render(request, 'contact.html', {'contact' : contact})

def mrph(request):
    # Send a simple HTML response
    return render(request, 'mr-ph.html', {'mr-ph' : mr-ph})

def msph(request):
    return render(request, 'ms-ph.html', {'ms-ph' : ms-ph})

def sling(request):
    return render(request, 'sling-it.html', {'sling-it' : sling-it})

def tattoos(request):
    return render(request, 'tattoos.html', {'tattoos' : tattoos})

def artists(request):
    return render(request, 'artists.html', {'artists' : artists})

def pix(request):
    return render(request, 'pix.html', {'pix' : pix})

def events(request):
    return render(request, 'events.html', {'event' : event})

def map(request):
    return render(request, 'map', {'map': map})
