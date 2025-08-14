"""
Configuración de sitemaps para mejorar el SEO de SecuKids
"""

from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    """Sitemap para las páginas estáticas de SecuKids"""
    priority = 1.0
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        """Lista de todas las páginas/vistas del sitio"""
        return [
            'juegos:home',  # Página principal
            'juegos:secuencia_animales',  # Juego de secuencia de animales
            'juegos:secuencia_colores',  # Juego de secuencia de colores
            'juegos:secuencia_eventos',  # Juego de secuencia de eventos
            'juegos:memoria_cartas',  # Juego de memoria de cartas
            'juegos:rompecabezas',  # Juego de rompecabezas
        ]

    def location(self, item):
        """Genera la URL para cada item"""
        return reverse(item)

    def priority(self, item):
        """Define la prioridad de cada página"""
        if item == 'juegos:home':
            return 1.0  # La página principal tiene máxima prioridad
        else:
            return 0.8  # Los juegos tienen alta prioridad

    def changefreq(self, item):
        """Define con qué frecuencia cambia cada página"""
        if item == 'juegos:home':
            return 'daily'  # La home puede cambiar diariamente
        else:
            return 'weekly'  # Los juegos cambian menos frecuentemente


class GamesSitemap(Sitemap):
    """Sitemap específico para los juegos educativos"""
    priority = 0.9
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        """Lista específica de juegos con sus descripciones"""
        return [
            {
                'url_name': 'juegos:secuencia_animales',
                'title': 'Secuencia de Animales - Juego de Memoria Auditiva',
                'description': 'Juego educativo para desarrollar memoria auditiva con sonidos de animales'
            },
            {
                'url_name': 'juegos:secuencia_colores', 
                'title': 'Secuencia de Colores - Juego de Memoria Visual',
                'description': 'Juego educativo para desarrollar memoria visual con secuencias de colores'
            },
            {
                'url_name': 'juegos:secuencia_eventos',
                'title': 'Secuencia de Eventos - Juego de Lógica Temporal',
                'description': 'Juego educativo para desarrollar pensamiento lógico y comprensión temporal'
            },
            {
                'url_name': 'juegos:memoria_cartas',
                'title': 'Memoria de Cartas - Juego de Concentración',
                'description': 'Juego educativo clásico de memoria para fortalecer la concentración'
            },
            {
                'url_name': 'juegos:rompecabezas',
                'title': 'Rompecabezas Interactivo - Juego de Habilidades Espaciales',
                'description': 'Juego educativo para desarrollar habilidades espaciales y coordinación'
            },
        ]

    def location(self, item):
        """Genera la URL para cada juego"""
        return reverse(item['url_name'])
