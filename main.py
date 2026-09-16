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

def formato_moneda(valor):
    return f"${valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def buscar_producto(codigo):
    for p in productos:
        if p["codigo"] == codigo.upper():
            return p
    return None

def menu_productos():
    while True:
        print("\n" + "=" * 60)
        print(f"{'GESTION DE PRODUCTOS':^60}")
        print("=" * 60)
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Actualizar producto")
        print("4. Desactivar producto")
        print("5. Volver al menu principal")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            desactivar_producto()
        elif opcion == "5":
            break
        else:
            print("Opcion invalida.")

def registrar_producto():
    print("\n--- REGISTRAR PRODUCTO ---")
    codigo = input("Codigo del producto: ").strip().upper()
    if not codigo or buscar_producto(codigo):
        print("ERROR: Codigo invalido o ya registrado.")
        return

    nombre = input("Nombre del producto: ").strip()
    categoria = input("Categoria: ").strip()
    unidad = input("Unidad de medida: ").strip()

    try:
        precio_base = float(input("Precio base de venta: "))
        costo_base = float(input("Costo unitario de produccion: "))
        stock_minimo = int(input("Stock minimo de alerta: "))

        if precio_base <= 0 or costo_base < 0 or stock_minimo < 0:
            print("ERROR: Precios y costos deben ser validos.")
            return
    except ValueError:
        print("ERROR: Ingrese valores numericos validos.")
        return

    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "unidad": unidad,
        "precio_base": precio_base,
        "costo_base": costo_base,
        "stock_minimo": stock_minimo,
        "activo": True
    }
    productos.append(nuevo_producto)
    guardar_datos()
    print(f"SUCCESS: Producto '{nombre}' registrado correctamente.")

def listar_productos():
    print("\n" + "=" * 80)
    print(f"{'LISTADO GENERAL DE PRODUCTOS':^80}")
    print("=" * 80)
    if not productos:
        print("No hay productos registrados.")
        return

    print(f"+{'-'*12}+{'-'*22}+{'-'*15}+{'-'*12}+{'-'*10}+{'-'*10}+")
    print(f"| {'CODIGO':<10} | {'NOMBRE':<20} | {'PRECIO VENTA':<13} | {'COSTO U.':<10} | {'MINIMO':<8} | {'ESTADO':<8} |")
    print(f"+{'-'*12}+{'-'*22}+{'-'*15}+{'-'*12}+{'-'*10}+{'-'*10}+")
    for p in productos:
        costo = p.get("costo_base", 0.0)
        estado = "ACTIVO" if p["activo"] else "INACTIVO"
        print(f"| {p['codigo']:<10} | {p['nombre']:<20} | {formato_moneda(p['precio_base']):<13} | {formato_moneda(costo):<10} | {p['stock_minimo']:<8} | {estado:<8} |")
    print(f"+{'-'*12}+{'-'*22}+{'-'*15}+{'-'*12}+{'-'*10}+{'-'*10}+")

def actualizar_producto():
    print("\n--- ACTUALIZAR PRODUCTO ---")
    codigo = input("Codigo del producto: ").strip().upper()
    p = buscar_producto(codigo)
    if not p:
        print("ERROR: Producto no encontrado.")
        return

    nombre = input(f"Nuevo nombre [{p['nombre']}]: ").strip()
    precio = input(f"Nuevo precio [{p['precio_base']}]: ").strip()
    costo = input(f"Nuevo costo [{p.get('costo_base', 0.0)}]: ").strip()

    if nombre:
        p["nombre"] = nombre
    if precio:
        try:
            p["precio_base"] = float(precio)
        except ValueError:
            pass
    if costo:
        try:
            p["costo_base"] = float(costo)
        except ValueError:
            pass

    guardar_datos()
    print("SUCCESS: Producto actualizado correctamente.")

def desactivar_producto():
    codigo = input("\nCodigo del producto a desactivar: ").strip().upper()
    p = buscar_producto(codigo)
    if not p:
        print("ERROR: Producto no encontrado.")
        return

    p["activo"] = False
    guardar_datos()
    print(f"SUCCESS: Producto '{p['nombre']}' desactivado.")

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