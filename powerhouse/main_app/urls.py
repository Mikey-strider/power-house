from django.urls import path

from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('current/', views.current, name='current'),
    path('staff-past/', views.staff, name='staff-past'),
    path('bar-history/', views.history, name='bar-history'),
    path('contact/', views.contact, name='contact'),
    path('mr-ph/', views.mrph, name='mr-ph'),
    path('ms-ph/', views.msph, name='ms-ph'),
    path('sling-it/', views.sling, name='sling-it'),
    path('tattoos/', views.tattoos, name='tattoos'),
    path('artists/', views.artists, name='artists'),
    path('pix/', views.pix, name='pix'),
    path('events/', views.events, name='events'),
    path('map/', views.map, name='map'),
]