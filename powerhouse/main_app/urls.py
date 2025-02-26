from django.urls import path

from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/current/', views.about.current, name='current'),
    path('about/staff-past/', views.about.staff-past, name='staff-past'),
    path('about/bar-history/', views.about.bar-history, name='bar-history'),
    path('about/contact/', views.about.contact, name='contact'),
    path('about/mr-ph/', views.about.mr-ph, name='mr-ph'),
    path('about/ms-ph/', views.about.ms-ph, name='ms-ph'),
    path('about/sling-it/', views.about.sling-it, name='sling-it'),
    path('about/tattos/', views.about.tattoos, name='tattoos')
]