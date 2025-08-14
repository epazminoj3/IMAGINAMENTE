from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Juego

def robots_txt(request):
    """Vista para servir robots.txt para SEO"""
    content = """User-agent: *
Allow: /

# Sitemap
Sitemap: https://secukids.onrender.com/sitemap.xml

# Optimización para buscadores
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# Evitar indexar archivos administrativos
Disallow: /admin/
Disallow: /static/admin/

# Permitir todos los juegos educativos
Allow: /secuencia-animales/
Allow: /secuencia-colores/
Allow: /secuencia-eventos/
Allow: /memoria-cartas/
Allow: /rompecabezas/
"""
    return HttpResponse(content, content_type="text/plain")

def google_verification(request):
    """Vista para servir el archivo de verificación de Google Search Console"""
    content = "google-site-verification: googleaad70d051055900d.html"
    return HttpResponse(content, content_type="text/html")

def home(request):
    """Vista para la página principal con SEO optimizado"""
    context = {
        'titulo': 'SecuKids - Juegos Educativos para Niños',
        'descripcion': 'Plataforma educativa interactiva con juegos para desarrollar memoria, concentración y habilidades cognitivas en niños. ¡Aprende jugando!',
        'meta_description': 'SecuKids ofrece juegos educativos interactivos para niños: secuencia de animales, colores, rompecabezas y más. Desarrolla memoria y habilidades cognitivas jugando.',
        'meta_keywords': 'juegos educativos, memoria para niños, juegos interactivos, educación infantil, desarrollo cognitivo, aprendizaje lúdico, secukids',
        'og_title': 'SecuKids - Juegos Educativos Interactivos',
        'og_description': 'Plataforma educativa con juegos para desarrollar memoria, concentración y habilidades cognitivas en niños',
        'og_image': 'https://secukids.onrender.com/static/images/secukids_logo.png',
        'canonical_url': 'https://secukids.onrender.com/',
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
    """Vista para el juego de secuencia de animales con SEO"""
    context = {
        'titulo': 'Secuencia de Animales - Juego de Memoria Auditiva | SecuKids',
        'descripcion': 'Juego educativo para desarrollar memoria auditiva. Escucha los sonidos de animales y ordénalos correctamente. ¡Perfecto para niños!',
        'meta_description': 'Juego de secuencia de animales para desarrollar memoria auditiva en niños. Escucha sonidos de perro, gato, vaca y más. Educativo y divertido.',
        'meta_keywords': 'juego animales, memoria auditiva, sonidos animales, educación infantil, desarrollo auditivo, secukids',
        'og_title': 'Secuencia de Animales - Juego de Memoria Auditiva',
        'og_description': 'Desarrolla la memoria auditiva de tu hijo con nuestro juego de secuencia de animales',
        'canonical_url': 'https://secukids.onrender.com/secuencia-animales/',
    }
    return render(request, 'juegos/secuencia_animales.html', context)

def secuencia_colores(request):
    """Vista para el juego de secuencia de colores con SEO"""
    context = {
        'titulo': 'Secuencia de Colores - Juego de Memoria Visual | SecuKids',
        'descripcion': 'Juego educativo de memoria visual con colores. Observa las secuencias y repítelas para desarrollar concentración y memoria.',
        'meta_description': 'Juego de secuencia de colores para desarrollar memoria visual en niños. Observa patrones de colores y repítelos. Mejora concentración y memoria.',
        'meta_keywords': 'juego colores, memoria visual, patrones colores, concentración niños, desarrollo cognitivo, secukids',
        'og_title': 'Secuencia de Colores - Juego de Memoria Visual',
        'og_description': 'Desarrolla la memoria visual y concentración con nuestro juego de secuencia de colores',
        'canonical_url': 'https://secukids.onrender.com/secuencia-colores/',
    }
    return render(request, 'juegos/secuencia_colores.html', context)

def secuencia_eventos(request):
    """Vista para el juego de secuencia de eventos con SEO"""
    context = {
        'titulo': 'Secuencia de Eventos - Juego de Lógica Temporal | SecuKids',
        'descripcion': 'Juego educativo para desarrollar pensamiento lógico y comprensión temporal. Ordena eventos en secuencia correcta.',
        'meta_description': 'Juego de secuencia de eventos para desarrollar lógica temporal en niños. Ordena actividades diarias y eventos en secuencia correcta.',
        'meta_keywords': 'secuencia eventos, lógica temporal, pensamiento lógico, orden cronológico, educación infantil, secukids',
        'og_title': 'Secuencia de Eventos - Juego de Lógica Temporal',
        'og_description': 'Desarrolla el pensamiento lógico y comprensión temporal con nuestro juego de secuencia de eventos',
        'canonical_url': 'https://secukids.onrender.com/secuencia-eventos/',
    }
    return render(request, 'juegos/secuencia_eventos.html', context)

def memoria_cartas(request):
    """Vista para el juego de memoria de cartas con SEO"""
    context = {
        'titulo': 'Memoria de Cartas - Juego de Concentración | SecuKids',
        'descripcion': 'Juego clásico de memoria con cartas. Encuentra los pares iguales y desarrolla concentración y memoria a corto plazo.',
        'meta_description': 'Juego de memoria con cartas para niños. Encuentra pares iguales, desarrolla concentración y memoria a corto plazo. Clásico educativo.',
        'meta_keywords': 'memoria cartas, concentración niños, juego parejas, memoria corto plazo, desarrollo cognitivo, secukids',
        'og_title': 'Memoria de Cartas - Juego de Concentración',
        'og_description': 'Mejora la concentración y memoria a corto plazo con nuestro juego de memoria de cartas',
        'canonical_url': 'https://secukids.onrender.com/memoria-cartas/',
    }
    return render(request, 'juegos/memoria_cartas.html', context)

def rompecabezas(request):
    """Vista para el juego de rompecabezas con SEO"""
    context = {
        'titulo': 'Rompecabezas Interactivo - Juego de Habilidades Espaciales | SecuKids',
        'descripcion': 'Rompecabezas interactivo para desarrollar habilidades espaciales y coordinación visomotora. Arrastra las piezas y completa las imágenes.',
        'meta_description': 'Rompecabezas interactivo para niños. Desarrolla habilidades espaciales, coordinación y resolución de problemas. Arrastra y completa imágenes.',
        'meta_keywords': 'rompecabezas interactivo, habilidades espaciales, coordinación visomotora, resolución problemas, desarrollo motor, secukids',
        'og_title': 'Rompecabezas Interactivo - Habilidades Espaciales',
        'og_description': 'Desarrolla habilidades espaciales y coordinación con nuestro rompecabezas interactivo',
        'canonical_url': 'https://secukids.onrender.com/rompecabezas/',
    }
    return render(request, 'juegos/rompecabezas.html', context)

def diagnostico_sonidos(request):
    """Vista para diagnosticar problemas con los sonidos"""
    context = {
        'titulo': 'Diagnóstico de Sonidos',
        'descripcion': 'Herramienta para verificar el estado de los archivos de audio',
    }
    return render(request, 'juegos/diagnostico_sonidos.html', context)
