import requests
import urllib.parse

URL_RUTA = "https://graphhopper.com/api/1/route?"
URL_GEOCODIFICACION = "https://graphhopper.com/api/1/geocode?"
CLAVE = "TU_API_KEY"  # Reemplazar por el token generado en GraphHopper
SALIR = ("s", "salir")


def quiere_salir(texto):
    """Devuelve True si el usuario escribió 's' o 'salir' (sin importar mayúsculas)."""
    return texto.strip().lower() in SALIR


def pedir(mensaje):
    """Pide un dato al usuario y repite la pregunta si lo deja vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Debe ingresar un valor.")
            continue
        return texto


def geocodificar(ubicacion, clave):
    """Convierte un nombre de lugar en coordenadas usando la API de geocodificación."""
    url = URL_GEOCODIFICACION + urllib.parse.urlencode(
        {"q": ubicacion, "limit": "1", "locale": "es", "key": clave}
    )
    respuesta = requests.get(url)
    estado = respuesta.status_code
    datos = respuesta.json()

    if estado == 200 and len(datos["hits"]) != 0:
        hit = datos["hits"][0]
        lat = hit["point"]["lat"]
        lng = hit["point"]["lng"]
        tipo = hit["osm_value"]
        partes = [p for p in (hit["name"], hit.get("state", ""), hit.get("country", "")) if p]
        nombre = ", ".join(partes)
        print(f"URL de la API de geocodificación para {nombre} (Tipo de ubicación: {tipo})\n{url}")
        return estado, lat, lng, nombre

    if estado != 200:
        print(f"Estado de la API de geocodificación: {estado}\nMensaje de error: {datos.get('message', '')}")
    else:
        print(f"No se encontró la ubicación: {ubicacion}")
    return estado, None, None, ubicacion


def mostrar_ruta(origen, destino, clave):
    """Consulta la API de rutas e imprime distancia, duración y narrativa en español."""
    parametros = [
        ("key", clave),
        ("locale", "es"),  # instrucciones del viaje en español
        ("point", f"{origen[1]},{origen[2]}"),
        ("point", f"{destino[1]},{destino[2]}"),
    ]
    url = URL_RUTA + urllib.parse.urlencode(parametros)
    respuesta = requests.get(url)
    estado = respuesta.status_code
    datos = respuesta.json()

    print(f"Estado de la API de rutas: {estado}\nURL de la API de rutas:\n{url}")
    print("=================================================")
    print(f"Indicaciones desde {origen[3]} hasta {destino[3]}")
    print("=================================================")

    if estado != 200:
        print(f"Mensaje de error: {datos.get('message', '')}")
        print("*************************************************")
        return

    ruta = datos["paths"][0]
    km = ruta["distance"] / 1000
    millas = km / 1.61
    segundos_totales = int(ruta["time"] / 1000)
    horas, resto = divmod(segundos_totales, 3600)
    minutos, segundos = divmod(resto, 60)

    print(f"Distancia recorrida: {millas:.2f} millas / {km:.2f} km")
    print(f"Duración del viaje: {horas:02d}:{minutos:02d}:{segundos:02d}")
    print("=================================================")
    print("Narrativa del viaje:")
    for paso in ruta["instructions"]:
        dist_km = paso["distance"] / 1000
        print(f"{paso['text']} ( {dist_km:.2f} km / {dist_km / 1.61:.2f} millas )")
    print("=================================================")


def main():
    print("Escriba 's' o 'salir' en cualquier momento para terminar el programa.")
    while True:
        lugar_origen = pedir("Ubicación de origen: ")
        if quiere_salir(lugar_origen):
            break
        origen = geocodificar(lugar_origen, CLAVE)

        lugar_destino = pedir("Destino: ")
        if quiere_salir(lugar_destino):
            break
        destino = geocodificar(lugar_destino, CLAVE)
        print("=================================================")

        if origen[1] is not None and destino[1] is not None:
            mostrar_ruta(origen, destino, CLAVE)
        else:
            print("No se pudo calcular la ruta. Intente con otras ubicaciones.")

    print("Programa finalizado.")


if __name__ == "__main__":
    main()
