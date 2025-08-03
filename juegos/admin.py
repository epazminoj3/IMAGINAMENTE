from django.contrib import admin
from .models import Juego, ImagenSecuencia

class ImagenSecuenciaInline(admin.TabularInline):
    model = ImagenSecuencia
    extra = 1

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel')
    inlines = [ImagenSecuenciaInline]

admin.site.register(ImagenSecuencia)