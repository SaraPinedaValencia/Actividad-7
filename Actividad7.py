from dataclasses import dataclass

from typing import List


@dataclass
class Elemento:
    nombre: str

    # Metodo especial de igualdad
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Elemento):
            return self.nombre == __o.nombre
        return False


class Conjunto:
    contador = 0

    def __init__(self, nombre: str):
        self.lista_elementos: List[Elemento] = []
        self.nombre: str = nombre
        Conjunto.contador += 1
        self.__id: int = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def setID(self, id):
        self.__id = id

    # Metodo contiene
    def contiene(self, elemento: Elemento) -> bool:
        for i in range(len(self.lista_elementos)):
            if elemento.nombre == self.lista_elementos[i].nombre:
                return True
            return False

    # Metodo agregar_elemento
    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.lista_elementos.append(elemento)
        else:
            return

    # Metodo unir
    def unir(self, otro_conjunto: object):
        if isinstance(otro_conjunto, Conjunto):
            for elemento in otro_conjunto.lista_elementos:
                self.agregar_elemento(elemento)
        else:
            return

    # Metodo add
    def __add__(self, otro_conjunto):
        resultado = Conjunto(self.nombre + " + " + otro_conjunto.nombre)
        resultado.lista_elementos = self.lista_elementos.copy()
        resultado.unir(otro_conjunto)
        return resultado

    # Metodo intersectar
    def intersectar(cls, conjunto1, conjunto2):
        resultado = Conjunto(conjunto1.nombre + " INTERSECTADO " + conjunto2.nombre)
        for elemento in conjunto1.lista_elementos:
            if conjunto2.contiene(elemento):
                resultado.lista_elementos.append(elemento)
        return resultado

    # Metodo str
    def __str__(self):
        nombres_elementos = [elemento.nombre for elemento in self.lista_elementos]
        return "Conjunto " + self.nombre + ": (" + ", ".join(nombres_elementos) + ")"