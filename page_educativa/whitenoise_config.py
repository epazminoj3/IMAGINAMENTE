from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
import os

def application_with_static(environ, start_response):
    """
    WSGI application that serves both Django app and static files including media
    """
    django_app = get_wsgi_application()
    
    # Configurar WhiteNoise para servir archivos estáticos y media
    static_app = WhiteNoise(django_app)
    
    # Agregar directorios estáticos
    static_app.add_files(os.path.join(os.path.dirname(__file__), '..', 'staticfiles'), prefix='/static/')
    static_app.add_files(os.path.join(os.path.dirname(__file__), '..', 'media'), prefix='/media/')
    static_app.add_files(os.path.join(os.path.dirname(__file__), '..', 'static'), prefix='/static/')
    
    return static_app(environ, start_response)
