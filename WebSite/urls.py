from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'Home'),
    path('QuienesSomos',views.quienes_somos, name = 'QuienesSomos'),
    path('Inmobiliaria',views.inmobiliaria, name = 'Inmobiliaria'),
    path('Regaleria',views.regaleria, name = 'Regaleria'),
    path('Contacto',views.contacto, name = 'Contacto'),
]