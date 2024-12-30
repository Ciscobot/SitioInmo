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

######################### PLANTILLAS #########################
def index(request):
    return render(request, 'plantillas/index.html')

def galeria(request):
    return render(request, 'plantillas/gallery.html')

def sobrenosotros(request):
    return render(request, 'plantillas/about.html')

def productos(request):
    return render(request, 'plantillas/products.html')

def contac(request):
    return render(request, 'plantillas/contact.html')