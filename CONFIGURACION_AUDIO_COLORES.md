# 🌈 Configuración de Audio para Secuencia de Colores

## 📁 Estructura de Archivos de Audio

Para que el juego funcione correctamente, necesitas agregar los siguientes archivos de audio en la carpeta:
`/media/sounds/`

### 🎨 Archivos de Audio de Colores (REQUERIDOS)

Cada color necesita su propio archivo de audio. Los nombres deben ser exactos:

```
📦 media/sounds/
 ┣ 📜 rojo.mp3          # Sonido para el color rojo
 ┣ 📜 azul.mp3          # Sonido para el color azul  
 ┣ 📜 amarillo.mp3      # Sonido para el color amarillo
 ┣ 📜 verde.mp3         # Sonido para el color verde
 ┣ 📜 morado.mp3        # Sonido para el color morado
 ┗ 📜 naranja.mp3       # Sonido para el color naranja
```

### 🎵 Archivos de Audio del Juego (OPCIONALES)

Estos archivos mejorarán la experiencia del juego:

```
📦 media/sounds/
 ┣ 📜 correcto.mp3              # Sonido cuando se acierta
 ┣ 📜 incorrecto.mp3            # Sonido cuando se falla
 ┣ 📜 inicio_colores.mp3        # Sonido al iniciar el juego
 ┣ 📜 completado_colores.mp3    # Sonido al completar el juego
 ┗ 📜 instrucciones_colores.mp3 # Sonido para las instrucciones
```

## 🎼 Frecuencias Sintéticas por Color

Si no tienes archivos de audio, el juego generará sonidos sintéticos con estas frecuencias:

- **🔴 Rojo**: 261.63 Hz (Do)
- **🔵 Azul**: 329.63 Hz (Mi)  
- **🟡 Amarillo**: 392.00 Hz (Sol)
- **🟢 Verde**: 523.25 Hz (Do octava alta)
- **🟣 Morado**: 659.25 Hz (Mi octava alta)
- **🟠 Naranja**: 783.99 Hz (Sol octava alta)

## 📋 Formatos Compatibles

El juego soporta los siguientes formatos de audio:
- **MP3** (recomendado)
- **WAV** 
- **OGG**

## 🔧 Configuración Avanzada

### Personalizar Colores y Sonidos

Si quieres cambiar los colores o frecuencias, edita el archivo:
`juegos/templates/juegos/secuencia_colores.html`

En la línea donde está definido el array `this.colors`:

```javascript
this.colors = [
    { name: 'Rojo', audioFile: 'rojo', frequency: 261.63, duration: 0.5, colorCode: '#FF6B6B' },
    { name: 'Azul', audioFile: 'azul', frequency: 329.63, duration: 0.5, colorCode: '#4ECDC4' },
    // ... agregar más colores aquí
];
```

### Agregar Nuevos Colores

1. Agrega el nuevo color al array `this.colors`
2. Crea el archivo de audio correspondiente
3. Agrega el estilo CSS para el nuevo color en la sección de estilos

## 🎮 Funcionalidades del Juego

- **10 niveles progresivos** de dificultad
- **Sistema de puntuación** acumulativa
- **Feedback visual y auditivo** para aciertos/errores
- **Diseño responsive** para móviles y PC
- **Instrucciones interactivas** con animación
- **Fallback a sonidos sintéticos** si no hay archivos

## 🚀 ¡Listo para Jugar!

Una vez que hayas agregado los archivos de audio, el juego estará completamente funcional. Los estudiantes podrán:

1. Escuchar la secuencia de sonidos de colores
2. Arrastrar los colores en el orden correcto  
3. Recibir feedback inmediato
4. Avanzar por 10 niveles de dificultad creciente

¡Disfruta enseñando con este juego educativo y musical! 🎉
