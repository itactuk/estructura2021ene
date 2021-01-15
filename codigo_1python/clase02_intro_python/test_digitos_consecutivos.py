import unittest
from codigo_1python.clase02_intro_python import digitos_consecutivos as p


class MyTestCase(unittest.TestCase):
    def test_comienzo(self):
        self.assertEqual(p.contar_digitos_consecutivos("4343jkljk"), 4)

    def test_medio(self):
        self.assertEqual(p.contar_digitos_consecutivos("dfd4343jk34ljk"), 6)

    def test_final(self):
        self.assertEqual(p.contar_digitos_consecutivos("dfdjkljk434"), 3)

    def test_no_consecutivos(self):
        self.assertEqual(p.contar_digitos_consecutivos("dfd4343jk4ljk"), 4)

    def test_vacio(self):
        self.assertEqual(p.contar_digitos_consecutivos(""), 0)

    def test_no_numeros(self):
        self.assertEqual(p.contar_digitos_consecutivos("fdsfsdfssff"), 0)


if __name__ == '__main__':
    unittest.main()
