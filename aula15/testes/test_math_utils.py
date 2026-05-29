import unittest
from aula15.testes.math_utils import somar, eh_par

class TestMathUtils(unittest.TestCase):
    def test_somar_basico(self):
        resultado = somar(2, 2)
        self.assertEqual(resultado, 4)
        #self.assertEqual(resultado, 3)
        self.assertNotEqual(resultado, 5)
        #self.assertNotEqual(resultado, 4)

    def test_eh_par_exemplos(self):
        for num, esperado in [(0, True), (1, False), (2, True), (-3, False)]:
            with self.subTest(num = num):
                self.assertEqual(eh_par(num), esperado)

    def test_asserts_varios(self):
        numeros = [1, 2, 3]
        self.assertTrue(eh_par(2))
        self.assertFalse(eh_par(3))
        self.assertIn(2, numeros)
        self.assertNotIn(4, numeros)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    # Em scripts normais, pode ser apenas: unittest.main()