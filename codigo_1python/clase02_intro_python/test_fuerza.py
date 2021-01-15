import unittest
from codigo_1python.clase02_intro_python import fuerza


class MyTestCase(unittest.TestCase):
    def test_calcular_fueza(self):
        resultado = fuerza.calc_fuerza(3, 4)
        valor_esperado = 12
        self.assertEqual(resultado, valor_esperado)


if __name__ == '__main__':
    unittest.main()
