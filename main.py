import json
import os
from datetime import datetime

DATA_DIR = "data"
PRODUCTOS_FILE = os.path.join(DATA_DIR, "productos.json")
LOTES_FILE = os.path.join(DATA_DIR, "lotes.json")
MOVIMIENTOS_FILE = os.path.join(DATA_DIR, "movimientos.json")
VENTAS_FILE = os.path.join(DATA_DIR, "ventas.json")

productos = []
lotes = []
movimientos = []
ventas = []

def cargar_json(ruta):
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error al cargar {ruta}: {e}")
        return []

def cargar_datos():
    global productos, lotes, movimientos, ventas
    os.makedirs(DATA_DIR, exist_ok=True)
    productos = cargar_json(PRODUCTOS_FILE)
    lotes = cargar_json(LOTES_FILE)
    movimientos = cargar_json(MOVIMIENTOS_FILE)
    ventas = cargar_json(VENTAS_FILE)

def guardar_json(ruta, datos):
    try:
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error al guardar en {ruta}: {e}")

def guardar_datos():
    guardar_json(PRODUCTOS_FILE, productos)
    guardar_json(LOTES_FILE, lotes)
    guardar_json(MOVIMIENTOS_FILE, movimientos)
    guardar_json(VENTAS_FILE, ventas)

def menu_principal():
    while True:
        print("\n" + "=" * 60)
        print(f"{'AGROCONTROL CBA - SENA':^60}")
        print("=" * 60)
        print("1. Gestion de Productos")
        print("2. Gestion de Lotes Productivos")
        print("3. Movimientos de Inventario")
        print("4. Ventas y Devoluciones")
        print("5. Reportes y Exportacion CSV")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "6":
            print("\nSaliendo del sistema...")
            break

if __name__ == "__main__":
    menu_principal()