"""
Vista para verificación de Google Search Console
"""

from django.http import HttpResponse

def google_verification(request):
    """Vista para servir el archivo de verificación de Google Search Console"""
    # Reemplaza 'your-verification-code' con el código real de Google Search Console
    content = "google-site-verification: googleXXXXXXXXXXXXXXXX.html"
    return HttpResponse(content, content_type="text/plain")

def bing_verification(request):
    """Vista para verificación de Bing Webmaster Tools"""
    # Reemplaza con tu código de verificación de Bing
    content = '<meta name="msvalidate.01" content="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" />'
    return HttpResponse(content, content_type="text/html")
