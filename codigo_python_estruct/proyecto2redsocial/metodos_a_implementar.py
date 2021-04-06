# pueden implementarlos en una clase

import enum


class Parentesco(enum.Enum):
    padre = 1  # ó madre
    hijo = 2  # ó hija
    hermano = 3  # ó hermana
    tio = 4  # ó tía
    sobrino = 5  # ó sobrina
    primo_primero = 6
    primo_segundo = 7
    primo_tercero = 8
    primo_cuarto = 9
    no_contemplado = 10


def usuario_disponible(nombre_usario: str) -> bool:
    """
    Puede permitir falsos positivos.
    Tomar en cuenta que la cantidad de usarios es muy grande y podría ser que no quepa en la RAM
    :param nombre_usario:
    :return:
    """


def parentesco(id_persona1: int, id_persona2: int) -> Parentesco:
    """
    Determina el parentesco de persona1 con persona2.
    Si se retorna tío, se indica que la persona1 es tía de la persona2
    Si no es uno de los parentescos listados en la clase Parentesco, retornar Parentesco.no_contemplado
    :param id_persona1:
    :param id_persona2:
    :return:
    """


def distancia_de_amigos(id_persona1: int, id_persona2: int) -> int:
    """
    Indica la ruta más corta entre dos personas saltando entre los amigos de las personas.
    Por ej.: Si A es solamente amigo de B y B es solamanente amigo de C,
    entonces la distancia entre A y C es 1, porque tenemos que pasar por B para llegar a C
    Si la distancia es mayor que 10, retornar infinito
    :param id_persona1:
    :param id_persona2:
    :return:
    """


def tamano_red_de_familia(id_persona, distancia_maxima: int) -> int:
    """
    Cuenta la cantidad de miembros de la familia que tengan una distancia menor igual a distancia_maxima
    :param id_persona:
    :param distancia_maxima: la cantidad de nodos que se deben brincar para llegar a otro nodo
    :return:
    """


def buscar_por_nombre(nombre: str) -> int:
    """
    Buscar una persona por nombre y retornar su id
    :param nombre:
    :return: id_persona
    """
