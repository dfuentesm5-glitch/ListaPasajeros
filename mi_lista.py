from pasajero import Pasajero


class MiLista:
    """Lista construida a mano sobre un arreglo de tamaño fijo.
    datos     -> [p1, p2, p3, None, None, ...]
    capacidad -> total de cajones     cantidad -> cajones ocupados
    ⛔ Sin append, insert, pop, remove, sort, reverse, copy, len, in, slicing.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def añadir(self, pasajero):
        if self.cantidad == self.capacidad:
            print("  ⚠ La lista está llena")
            return False
        if self.buscar(pasajero.numero) != -1:        # mejora: sin números repetidos
            print(f"  ⚠ Ya existe el pasajero #{pasajero.numero}")
            return False
        self.datos[self.cantidad] = pasajero          # primer cajón libre
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):
        if self.cantidad == 0:
            print("  (lista vacía)")
            return
        for i in range(self.cantidad):
            print(f"  [{i}] {self.datos[i]}")

    # auxiliar: devuelve el pasajero de una posición (o None si no es válida)
    def obtener(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            return None
        return self.datos[posicion]

    # ---------------- Operaciones de la tabla 3.1 ----------------
    def insertar(self, posicion, pasajero):
        if self.cantidad == self.capacidad:
            print("  ⚠ La lista está llena")
            return False
        if posicion < 0 or posicion > self.cantidad:
            print(f"  ⚠ Posición inválida (debe estar entre 0 y {self.cantidad})")
            return False
        if self.buscar(pasajero.numero) != -1:
            print(f"  ⚠ Ya existe el pasajero #{pasajero.numero}")
            return False
        i = self.cantidad                             # correr a la DERECHA, de atrás hacia adelante
        while i > posicion:
            self.datos[i] = self.datos[i - 1]
            i = i - 1
        self.datos[posicion] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    def buscar(self, numero):                         # búsqueda lineal
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i
        return -1

    def buscar_binaria(self, numero):                 # requiere lista ordenada por numero
        izq = 0
        der = self.cantidad - 1
        while izq <= der:
            medio = (izq + der) // 2
            actual = self.datos[medio].numero
            if actual == numero:
                return medio
            elif numero < actual:
                der = medio - 1
            else:
                izq = medio + 1
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            print(f"  ⚠ Posición inválida (debe estar entre 0 y {self.cantidad - 1})")
            return None
        aux = self.datos[posicion]                    # guardamos al que se va
        for i in range(posicion, self.cantidad - 1):  # correr a la IZQUIERDA
            self.datos[i] = self.datos[i + 1]
        self.datos[self.cantidad - 1] = None          # último cajón queda vacío
        self.cantidad = self.cantidad - 1
        return aux

    def eliminar_por_valor(self, numero):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.eliminar_por_posicion(pos)
        return True

    def ordenar_asc(self):                            # burbuja, menor a mayor
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero > self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    def ordenar_desc(self):                           # igual, cambiando solo el símbolo
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero < self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    def reversar(self):                               # dos punteros
        izq = 0
        der = self.cantidad - 1
        while izq < der:
            aux = self.datos[izq]
            self.datos[izq] = self.datos[der]
            self.datos[der] = aux
            izq = izq + 1
            der = der - 1

    def copiar(self):
        nueva = MiLista(self.capacidad)
        for i in range(self.cantidad):
            nueva.añadir(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad