import os

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