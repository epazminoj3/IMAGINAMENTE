from django.urls import path
from . import views

app_name = 'juegos'  # Importante para namespacing

urlpatterns = [
    path('', views.home, name='home'),  # Página principal
    path('juegos/', views.lista_juegos, name='lista_juegos'),  # Lista de juegos
    path('juegos/<int:juego_id>/', views.juego_detalle, name='juego_detalle'),  # Detalle del juego
    path('secuencia-animales/', views.secuencia_animales, name='secuencia_animales'),  # Juego de secuencia de animales
    path('secuencia-colores/', views.secuencia_colores, name='secuencia_colores'),  # Juego de secuencia de colores
    path('secuencia-eventos/', views.secuencia_eventos, name='secuencia_eventos'),  # Juego de secuencia de eventos
    path('memoria-cartas/', views.memoria_cartas, name='memoria_cartas'),  # Juego de memoria de cartas
    path('rompecabezas/', views.rompecabezas, name='rompecabezas'),  # Juego de rompecabezas
    path('diagnostico-sonidos/', views.diagnostico_sonidos, name='diagnostico_sonidos'),  # Diagnóstico de sonidos
]