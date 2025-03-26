from django.http import HttpResponse
from django.shortcuts import render

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def current(request):
    return render(request, 'about/current.html', {'current' : current})

def staff(request):
    return render(request, 'about/staff-past.html', {'staff' : staff})

def history(request):
    return render(request, 'about/bar-history.html', {'history' : history})

def contact(request):
    return render(request, 'about/contact.html', {'contact' : contact})

def mrph(request):
    # Send a simple HTML response
    return render(request, 'about/mr-ph.html', {'mrph' : mrph})

def msph(request):
    return render(request, 'about/ms-ph.html', {'msph' : msph})

def sling(request):
    return render(request, 'about/sling-it.html', {'sling' : sling})

def tattoos(request):
    return render(request, 'about/tattoos.html', {'tattoos' : tattoos})

def artists(request):
    return render(request, 'about/artists.html', {'artists' : artists})

def pix(request):
    return render(request, 'pix.html', {'pix' : pix})

def events(request):
    return render(request, 'events.html', {'events' : events})

def map(request):
    return render(request, 'map', {'map': map})
