"""
URL configuration for page_educativa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from juegos.sitemaps import StaticViewSitemap, GamesSitemap
from juegos.views import robots_txt, google_verification

from django.conf import settings
from django.conf.urls.static import static

# Configuración de sitemaps para SEO
sitemaps_dict = {
    'static': StaticViewSitemap,
    'games': GamesSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('juegos.urls')),  # Aquí conectas tu app
    
    # SEO URLs
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps_dict}, name='django.contrib.sitemaps.views.sitemap'),
    
    # Google Search Console verification
    path('googleaad70d051055900d.html', google_verification, name='google_verification'),
]

# Servir archivos estáticos y media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
