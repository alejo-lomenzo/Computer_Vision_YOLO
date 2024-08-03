# Proyecto: La Nueva Generación - El Poder de la Detección

### Descripción

Este proyecto tiene como objetivo desarrollar un software para reconocer cartas españolas y calcular los puntos del envido en el juego de truco, utilizando modelos de reconocimiento de objetos como YOLO y técnicas avanzadas de programación. 

### Estructura del archivo `procesos_dataset`

1. **Implementación del Dataset**
   - Organización de las imágenes y etiquetas en directorios específicos.
   - Verificación de la correspondencia entre imágenes y etiquetas.
   - Dibujar cajas delimitadoras en las imágenes.

2. **Validación de Anotaciones**
   - Verificación y unificación de las anotaciones al formato YOLO.

3. **Aumentación del Dataset**
   - Uso de la biblioteca `Albumentations` para aplicar transformaciones aleatorias a las imágenes y poder aumentar el dataset.

4. **División de Datos**
   - División del dataset en conjuntos de entrenamiento, validación y prueba.

5. **Visualización del Dataset**
   - Uso de `FiftyOne` para explorar y evaluar los conjuntos de datos.
   - Visualizacion de la composicion de clases de mi dataset.

6. **Entrenamiento, Validación y Testeo de Modelos**
   - Entrenamiento de modelos YOLO y evaluación de su rendimiento.

### Estructura del archivo `prueba_modelo.py`

1. **Cargar el Modelo**
   - `load_model`: Carga y almacena en caché el modelo YOLO.

2. **Calcular Envido**
   - `calcular_envido`: Calcula el valor del envido basado en las cartas detectadas.

3. **Procesar Imagen**
   - `process_image`: Detecta cartas en una imagen, dibuja las detecciones y calcula el envido.

4. **Función Principal (`main`)**
   - **Interfaz de Usuario**: Ofrece opciones para "Subir imagen" o "Probar en vivo".
   - **Subir Imagen**: Procesa una imagen subida para detectar cartas y calcular el envido.
   - **Probar en Vivo**: Captura video en tiempo real con la cámara web para detectar cartas y calcular el envido.

5. **Detención de la Captura en Vivo**
   - Controla la captura de la cámara en vivo con un botón para detenerla.


### Instalación

Para ejecutar este proyecto, necesitas instalar las dependencias listadas en `requirements.txt`. Para hacerlo, puedes utilizar el siguiente comando:

```bash
pip install -r requirements.txt
