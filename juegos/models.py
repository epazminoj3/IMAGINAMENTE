from django.db import models

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel = models.CharField(max_length=50, choices=[
        ('Fácil', 'Fácil'),
        ('Medio', 'Medio'),
        ('Difícil', 'Difícil'),
    ])
    
    def __str__(self):
        return self.nombre

class ImagenSecuencia(models.Model):
    juego = models.ForeignKey(Juego, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='secuencias/')
    orden_correcto = models.PositiveIntegerField(help_text='Posición correcta de la imagen en la secuencia')

    def __str__(self):
        return f"{self.juego.nombre} - Imagen {self.orden_correcto}"

