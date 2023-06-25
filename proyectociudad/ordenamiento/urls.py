"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('parroquias', views.index, name='index'),
    path('parroquias/crear', views.crear_parroquia, name='crear_parroquia'),
    path('parroquias/editar/<int:id>', views.editar_parroquia, name='editar_parroquia'),
    path('parroquias/barrio/crear', views.crear_barrio, name='crear_barrio'),
    path('parroquias/barrio/editar/<int:id>', views.editar_barrio, name='editar_barrio'),
    # path('barrios', views.index, name='index'),

]
