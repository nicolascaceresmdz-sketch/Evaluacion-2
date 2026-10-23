# Calculadora de rutas con GraphHopper

Este programa permite calcular la ruta entre dos ubicaciones escritas por el usuario. Utiliza la API de **GraphHopper** para convertir los nombres de lugares en coordenadas y luego obtener la distancia, el tiempo estimado y las indicaciones del viaje en español.

## Requisitos

- Python 3 instalado en el computador.
- Conexión a Internet.
- Una clave de API gratuita de [GraphHopper](https://www.graphhopper.com/).
- La librería `requests`.

## Instalación

1. Descarga o clona este repositorio.
2. Abre una terminal en la carpeta del proyecto.
3. Instala la librería necesaria:

```bash
pip install requests
```

## Configuración

Antes de ejecutar el programa, debes agregar tu clave de API de GraphHopper.

1. Crea una cuenta en GraphHopper y genera una clave de API.
2. Abre el archivo `graphhopper_es.py`.
3. Busca esta línea:

```python
CLAVE = "TU_API_KEY"
```

4. Reemplaza `TU_API_KEY` por tu clave real, por ejemplo:

```python
CLAVE = "abcd1234tu_clave_real"
```

> **Importante:** No compartas tu clave de API ni la subas a un repositorio público.

## Uso

Ejecuta el programa desde la terminal:

```bash
python graphhopper_es.py
```

El programa te pedirá dos datos:

```text
Ubicación de origen:
Destino:
```

Puedes escribir nombres de ciudades, direcciones o lugares reconocibles, por ejemplo:

```text
Ubicación de origen: Santiago, Chile
Destino: Valparaíso, Chile
```

Después, el programa mostrará:

- La URL utilizada para consultar la API.
- La distancia del viaje en kilómetros y millas.
- La duración estimada del recorrido.
- Una lista con las indicaciones paso a paso en español.

## Ejemplo de salida

```text
Indicaciones desde Santiago, Chile hasta Valparaíso, Chile
=================================================
Distancia recorrida: 72.50 millas / 116.68 km
Duración del viaje: 01:25:30
=================================================
Narrativa del viaje:
Continúe hacia el sureste ( 0.15 km / 0.09 millas )
Gire a la derecha ( 1.20 km / 0.75 millas )
...
```

## Cómo salir

En cualquier momento, cuando el programa pida una ubicación, puedes escribir:

```text
s
```

o:

```text
salir
```

El programa finalizará inmediatamente.

## Posibles errores

| Mensaje o situación | Causa probable | Solución |
|---|---|---|
| `No se encontró la ubicación` | El nombre escrito no fue reconocido por GraphHopper | Escribe una dirección más completa, incluyendo ciudad y país |
| `Mensaje de error: ...` | La API devolvió un error | Revisa tu conexión, tu clave de API y los límites de uso |
| El programa no inicia | Falta instalar `requests` | Ejecuta `pip install requests` |
| Error de autenticación | La clave de API no fue configurada o es inválida | Reemplaza correctamente `TU_API_KEY` en el código |

## Estructura del proyecto

```text
.
├── graphhopper_es.py
└── README.md
```

## Créditos

Este programa utiliza la API pública de [GraphHopper](https://www.graphhopper.com/) para geocodificación y cálculo de rutas.