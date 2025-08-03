"""
WSGI config for page_educativa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'page_educativa.settings')

application = get_wsgi_application()

# Configurar WhiteNoise para servir archivos media también
if os.environ.get('RENDER'):
    application = WhiteNoise(application, root=os.path.join(os.path.dirname(__file__), '..', 'staticfiles'))
    # Agregar directorio media
    application.add_files(os.path.join(os.path.dirname(__file__), '..', 'media'), prefix='/media/')
