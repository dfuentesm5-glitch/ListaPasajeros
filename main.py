from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython

lista1 = MiLista(10)
lista2 = ListaPython()


# ------------------------- funciones de apoyo -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def cargar_datos_prueba(lista):
    datos = [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]
    añadidos = 0
    for p in datos:
        if lista.añadir(p):
            añadidos = añadidos + 1
    print(f"  ✓ Datos de prueba cargados ({añadidos} nuevos)")


def mostrar_opciones(titulo, extras=False):
    print(f"\n========== {titulo} ==========")
    print(" 1. Añadir           2. Listar            3. Insertar en posición")
    print(" 4. Buscar (lineal)  5. Buscar (binaria)  6. Modificar")
    print(" 7. Eliminar por posición                 8. Eliminar por número")
    print(" 9. Ordenar asc     10. Ordenar desc     11. Reversar")
    print("12. Copiar          13. Longitud")
    if extras:
        print("14. Filtrar por destino                  15. Mayores de edad")
    print(" C. Cargar datos de prueba                0. Volver")


def mostrar_busqueda(lista, pos):
    if pos == -1:
        print("  No existe")
    else:
        print(f"  Encontrado en [{pos}]: {lista.obtener(pos).nombre}")


def atender_opcion(lista, op, extras=False):
    """Patrón de cada opción: LEER -> LLAMAR -> MOSTRAR.
    Sirve para las dos listas porque tienen los mismos métodos.
    Devuelve False si la opción no es válida."""
    if op == "1":
        pasajero = leer_pasajero()                          # 1. LEER
        if lista.añadir(pasajero):                          # 2. LLAMAR
            print("  ✓ Pasajero añadido")                   # 3. MOSTRAR
    elif op == "2":
        lista.listar()
    elif op == "3":
        pos = leer_entero("  Posición: ")
        pasajero = leer_pasajero()
        if lista.insertar(pos, pasajero):
            print(f"  ✓ Insertado en [{pos}]")
    elif op == "4":
        numero = leer_entero("  N.º a buscar: ")
        mostrar_busqueda(lista, lista.buscar(numero))
    elif op == "5":
        print("  (la búsqueda binaria requiere la lista ordenada: usa antes la opción 9)")
        numero = leer_entero("  N.º a buscar: ")
        mostrar_busqueda(lista, lista.buscar_binaria(numero))
    elif op == "6":
        numero = leer_entero("  N.º del pasajero: ")
        destino = input("  Nuevo destino: ").strip()
        asiento = input("  Nuevo asiento: ").strip().upper()
        if lista.modificar(numero, destino, asiento):
            print("  ✓ Pasajero modificado")
        else:
            print("  No existe")
    elif op == "7":
        pos = leer_entero("  Posición a eliminar: ")
        eliminado = lista.eliminar_por_posicion(pos)
        if eliminado is not None:
            print(f"  ✓ Eliminado: {eliminado.nombre}; quedan {lista.longitud()}")
    elif op == "8":
        numero = leer_entero("  N.º a eliminar: ")
        if lista.eliminar_por_valor(numero):
            print(f"  ✓ Pasajero #{numero} eliminado")
        else:
            print("  No existe")
    elif op == "9":
        lista.ordenar_asc()
        lista.listar()
    elif op == "10":
        lista.ordenar_desc()
        lista.listar()
    elif op == "11":
        lista.reversar()
        lista.listar()
    elif op == "12":
        copia = lista.copiar()
        copia.reversar()
        print("  Copia reversada:")
        copia.listar()
        print("  Original (sin cambios):")
        lista.listar()
    elif op == "13":
        print(f"  Cantidad de pasajeros: {lista.longitud()}")
    elif op == "14" and extras:
        destino = input("  Destino: ").strip()
        resultado = lista.filtrar_por_destino(destino)
        if not resultado:
            print("  (ningún pasajero con ese destino)")
        for p in resultado:
            print(f"  {p}")
    elif op == "15" and extras:
        resultado = lista.mayores_de_edad()
        if not resultado:
            print("  (ningún mayor de edad)")
        for p in resultado:
            print(f"  {p}")
    elif op == "C":
        cargar_datos_prueba(lista)
    else:
        return False
    return True


# ---------------------- MENÚ 1 · MiLista ----------------------
def menu_lista1():
    while True:
        mostrar_opciones("MENÚ 1 · MiLista")
        op = input("Opción: ").strip().upper()
        if op == "0":
            break
        if not atender_opcion(lista1, op):
            print("  Opción no válida")


# ---------------------- MENÚ 2 · list de Python ----------------------
def menu_lista2():
    while True:
        mostrar_opciones("MENÚ 2 · list de Python", extras=True)
        op = input("Opción: ").strip().upper()
        if op == "0":
            break
        if not atender_opcion(lista2, op, extras=True):
            print("  Opción no válida")


# ---------------------- MENÚ PRINCIPAL ----------------------
def main():
    while True:
        print("\n===== TAREA LISTAS · PASAJEROS  =====")
        print("1. Menú 1 · MiLista")
        print("2. Menú 2 · list de Python")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_lista1()
        elif op == "2":
            menu_lista2()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()