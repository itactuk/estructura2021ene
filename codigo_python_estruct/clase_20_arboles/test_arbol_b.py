import os
from unittest import TestCase

from clase_20_arboles.arbol_b import ArbolB, ruta_base_archivo, obtener_ruta_nodo, obtener_ruta_data


class ArbolBTestCase(TestCase):

    def test_crear_arbol(self):
        arbol = ArbolB()
        with open(obtener_ruta_nodo(arbol.root.id)) as f:
            contenido = f.read()
        self.assertEqual('[true, 0, "'+arbol.root.id+'", [null, null, null, null, null, null], [null, null, null, null, null, null, null]]', contenido)

    def test_insert_en_arbol_vacio(self):
        arbol = ArbolB()
        llave = 1
        arbol.insert(llave, {"Nombre": "Ivan"})
        with open(obtener_ruta_nodo(arbol.root.id)) as f:
            contenido_nodo = f.read()
        self.assertEqual('[true, '+str(llave)+', "'+arbol.root.id+'"]', contenido_nodo)
        with open(obtener_ruta_data(llave)) as f:
            contenido_data = f.read()
        self.assertEqual('{"Nombre": "Ivan"}', contenido_data)

    def test_insert_en_arbol_con_nodo_lleno(self):
        arbol = ArbolB(t=2)
        llave_ivan = 1
        llave_waldry = 2
        llave_nic = 3
        llave_dante = 4
        arbol.insert(llave_ivan, {"Nombre": "Ivan"})
        arbol.insert(llave_waldry, {"Nombre": "Waldry"})
        arbol.insert(llave_nic, {"Nombre": "Nicol"})
        arbol.insert(llave_dante, {"Nombre": "Dante"})

        # verificamos root (Waldry)
        with open(obtener_ruta_nodo(arbol.root.id)) as f:
            contenido_root = f.read()
        self.assertEqual(2, arbol.root.count_children())
        self.assertEqual(1, arbol.root.count_keys())
        self.assertEqual(
            f'[false, 1, "'+arbol.root.id+f'", [null, {llave_waldry}, null, null], [null, "{arbol.root.children[1]}", "{arbol.root.children[2]}", null, null]]',
            contenido_root
        )
        with open(obtener_ruta_data(llave_nic)) as f:
            contenido_root_data = f.read()
        self.assertEqual('{"Nombre": "Nicol"}', contenido_root_data)

        # verificamos hijo izquierdo (Ivan)
        with open(obtener_ruta_nodo(arbol.root.id)) as f:
            contenido_root = f.read()
        self.assertEqual(0, arbol.root.count_children())
        self.assertEqual(1, arbol.root.count_keys())
        self.assertEqual(
            '[true, 2, "'+arbol.root.children[1]+f'", [{llave_ivan}]',
            contenido_root
        )
        with open(obtener_ruta_data(llave_ivan)) as f:
            contenido_root_data = f.read()
        self.assertEqual('{"Nombre": "Ivan"}', contenido_root_data)
        with open(obtener_ruta_data(llave_waldry)) as f:
            contenido_root_data = f.read()
        self.assertEqual('{"Nombre": "Waldry"}', contenido_root_data)

        # verificamos hijo derecho (Waldry+Dante)
        with open(obtener_ruta_nodo(arbol.root.id)) as f:
            contenido_root = f.read()
        self.assertEqual(0, arbol.root.count_children())
        self.assertEqual(2, arbol.root.count_keys())
        self.assertEqual(
            '[true, 1, "' + arbol.root.children[2] + f'", [{llave_waldry}, {llave_dante}]',
            contenido_root
        )
        with open(obtener_ruta_data(llave_dante)) as f:
            contenido_root_data = f.read()
        self.assertEqual('{"Nombre": "Dante"}', contenido_root_data)