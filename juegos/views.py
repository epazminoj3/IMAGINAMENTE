from django.shortcuts import render, get_object_or_404
from .models import Juego

def home(request):
    """Vista para la página principal"""
    context = {
        'titulo': 'Bienvenido a Página Educativa',
        'descripcion': 'Aprende jugando con nuestros juegos educativos',
    }
    return render(request, 'juegos/home.html', context)

def lista_juegos(request):
    """Vista para mostrar todos los juegos"""
    juegos = Juego.objects.all()
    return render(request, 'juegos/lista_juegos.html', {'juegos': juegos})

def juego_detalle(request, juego_id):
    """Vista para mostrar el detalle de un juego específico"""
    juego = get_object_or_404(Juego, pk=juego_id)
    imagenes = juego.imagenes.order_by('orden_correcto')
    return render(request, 'juegos/juego_detalle.html', {'juego': juego, 'imagenes': imagenes})

def secuencia_animales(request):
    """Vista para el juego de secuencia de animales"""
    context = {
        'titulo': 'Secuencia de Animales',
        'descripcion': '¡Escucha los sonidos de los animales y arrastra las imágenes en el orden correcto!',
    }
    return render(request, 'juegos/secuencia_animales.html', context)

def secuencia_colores(request):
    """Vista para el juego de secuencia de colores"""
    context = {
        'titulo': 'Secuencia de Colores',
        'descripcion': '¡Escucha los sonidos de los colores y arrastra los colores en el orden correcto!',
    }
    return render(request, 'juegos/secuencia_colores.html', context)

def secuencia_eventos(request):
    """Vista para el juego de secuencia de eventos"""
    context = {
        'titulo': 'Secuencia de Eventos',
        'descripcion': '¡Observa la secuencia correcta de eventos y ordénalos correctamente!',
    }
    return render(request, 'juegos/secuencia_eventos.html', context)

def memoria_cartas(request):
    """Vista para el juego de memoria de cartas"""
    context = {
        'titulo': 'Memoria de Cartas',
        'descripcion': '¡Encuentra todos los pares de cartas iguales usando tu memoria!',
    }
    return render(request, 'juegos/memoria_cartas.html', context)

def rompecabezas(request):
    """Vista para el juego de rompecabezas"""
    context = {
        'titulo': 'Rompecabezas',
        'descripcion': '¡Arrastra las piezas para completar las imágenes!',
    }
    return render(request, 'juegos/rompecabezas.html', context)

def diagnostico_sonidos(request):
    """Vista para diagnosticar problemas con los sonidos"""
    context = {
        'titulo': 'Diagnóstico de Sonidos',
        'descripcion': 'Herramienta para verificar el estado de los archivos de audio',
    }
    return render(request, 'juegos/diagnostico_sonidos.html', context)
