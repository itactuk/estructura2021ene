import unittest

from clase07_fuerza_bruta_max_sub_arr.msa_fuerza_bruta1 import encuentra_arreglo_suma_max as s1
from clase07_fuerza_bruta_max_sub_arr.msa_fuerza_bruta2 import encuentra_arreglo_suma_max as s2

from clase07_fuerza_bruta_max_sub_arr.msa_divide_y_venceras_1 import encuentra_arreglo_suma_max as s3


class Pruebas(unittest.TestCase):
    FUNCIONES = [
        ("s1", s1),
        ("s2", s2),
        ("s3_div_venc", s3),
    ]

    def test_1_un_solo_elemento_al_comienzo(self):
        arr = [13, -5, -25]
        for nombre, funcion in self.FUNCIONES:
            with self.subTest(nombre):
                i_inicial, i_final, suma = funcion(arr)
                self.assertEqual(i_inicial, 0)
                self.assertEqual(i_final, 0)
                self.assertEqual(suma, 13)

    def test_2_el_arreglo_completo(self):
        arr = [13, -5, 25]
        for nombre, funcion in self.FUNCIONES:
            with self.subTest(nombre):
                i_inicial, i_final, suma = funcion(arr)
                self.assertEqual(i_inicial, 0)
                self.assertEqual(i_final, 2)
                self.assertEqual(suma, 33)

    def test_3_ej_libro1(self):
        arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22,15, -4, 7]
        for nombre, funcion in self.FUNCIONES:
            with self.subTest(nombre):
                i_inicial, i_final, suma = funcion(arr)
                self.assertEqual(i_inicial, 7)
                self.assertEqual(i_final, 10)
                self.assertEqual(suma, 43)