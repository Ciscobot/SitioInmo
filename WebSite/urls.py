from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'Home'),
    path('QuienesSomos',views.quienes_somos, name = 'QuienesSomos'),
    path('Inmobiliaria',views.inmobiliaria, name = 'Inmobiliaria'),
    path('Regaleria',views.regaleria, name = 'Regaleria'),
    #path('Contacto',views.contacto, name = 'Contacto'),
    path('Galeria', views.galeria, name = 'Galeria'),
    path('SobreNosotros', views.sobrenosotros, name = 'SobreNosotros'),
    path('Productos', views.productos, name = 'Productos'),
    path('Contacto', views.contac, name = 'Contacto'),
]