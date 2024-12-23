from django.utils import timezone
from django.shortcuts import render 
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'plantillas/home.html')

def quienes_somos(request):
    return render(request,'plantillas/quienessomos.html' )

def inmobiliaria(request):
    return render(request, 'plantillas/inmobiliaria.html')

def regaleria(request):
    return render(request, 'plantillas/regaleria.html')

def contacto(request):
    return render(request, 'plantillas/contacto.html')
