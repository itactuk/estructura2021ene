import unittest

from clase_08_recurr.impl_merge_sort import ordena as msort
from clase_08_recurr.impl_quick_sort import ordena as qsort


class MyTestCase(unittest.TestCase):
    FUNCIONES = [
        ('merge', msort),
        ('qsort', qsort),
    ]

    def test_inv_impar(self):
        arr = [3, 2, 1]
        for nombre, ordena_fun in self.FUNCIONES:
            with self.subTest(nombre):
                arr = ordena_fun(arr)
                self.assertEqual(1, arr[0])
                self.assertEqual(2, arr[1])
                self.assertEqual(3, arr[2])

    def test_inv_par(self):
        arr = [5, 3, 2, 1]
        for nombre, ordena_fun in self.FUNCIONES:
            with self.subTest(nombre):
                arr = ordena_fun(arr)
                self.assertEqual(1, arr[0])
                self.assertEqual(2, arr[1])
                self.assertEqual(3, arr[2])
                self.assertEqual(5, arr[3])

    def test_ordenado(self):
        arr = [1, 2, 3]
        for nombre, ordena_fun in self.FUNCIONES:
            with self.subTest(nombre):
                arr = ordena_fun(arr)
                self.assertEqual(1, arr[0])
                self.assertEqual(2, arr[1])
                self.assertEqual(3, arr[2])


if __name__ == '__main__':
    unittest.main()
