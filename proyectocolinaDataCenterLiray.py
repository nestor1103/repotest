import unicodedata
import time
from colorama import init, Fore, Style 
# Inicializar colorama
init(autoreset=True)

# Definimos la lista de viajes
viajes = [
    {"tarifa": 60000, "direccion": "Camino del Acueducto 3460, Puente Alto"},
    {"tarifa": 41000, "direccion": "Sioux #1789, Maipu"},
    {"tarifa": 41000, "direccion": "Exequiel Fernández 6200, La Florida"},
    {"tarifa": 65000, "direccion": "Las Uvas y el Viento 0982, La Granja"},
    {"tarifa": 62000, "direccion": "Las Achiras 1319, Talagante"},
    {"tarifa": 26000, "direccion": "Jorge Luis Borges #164, Quilicura"},
    {"tarifa": 30000, "direccion": "Capilla Palacios #1387, Cerro Navia"},
    {"tarifa": 39000, "direccion": "Santa Elena 2837, San Joaquín"},
    {"tarifa": 34000, "direccion": "Avenida Las Torres #195, Estación Central"},
    {"tarifa": 24000, "direccion": "Novelista Januario Espinoza #2673, Colina"},
    {"tarifa": 38000, "direccion": "Pasaje Río Frío #9576, Pudahuel"},
]

def normalize_string(s):
    return ''.join(c.lower() for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn').strip()

def buscar_viajes_por_comuna(comuna):
    comuna_normalized = normalize_string(comuna)
    return [viaje for viaje in viajes if comuna_normalized in normalize_string(viaje['direccion'])]

def print_intermittent(text, times=3, delay=0.5):
    for _ in range(times):
        print(Fore.RED + Style.BRIGHT + text, end='\r')
        time.sleep(delay)
        print(' ' * len(text), end='\r')
        time.sleep(delay)
    print(Fore.RED + Style.BRIGHT + text)  # para imprimir intermitente rojo cuatico

# Ciclo principal
while True:
    comuna_busqueda = input("Ingrese el nombre de la comuna para buscar la tarifa:, (o cualquier número para salir): ")
    
    if comuna_busqueda.strip().isdigit():
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
    
    resultados = buscar_viajes_por_comuna(comuna_busqueda)

    if resultados:
        print(f"\nViajes encontrados para '{comuna_busqueda}':")
        for viaje in resultados:
            print(f"Tarifa: ${viaje['tarifa']}")
            print(f"Dirección: {viaje['direccion']}")
            print("-" * 200)
        
        tarifa_grande = max(viaje['tarifa'] for viaje in resultados)
        print("\nTarifa  encontrada:")
        print_intermittent(f"${tarifa_grande:,}", times=2)
    else:
        print(f"\nNo se encontraron viajes para '{comuna_busqueda}'.")
    
    print("\n" + "="*200 + "\n")
