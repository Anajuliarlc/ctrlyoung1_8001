import unittest
from aula15.testes.conta import ContaBancaria

class TestContaBancaria(unittest.TestCase):
    def setUp(self):
        self.conta = ContaBancaria("Ana", saldo_inicial=100.0)

    def test_depositar_incrementa_saldo(self):
        self.conta.depositar(50)
        self.assertEqual(self.conta.saldo, 150)

    def test_sacar_decrementa_saldo(self):
        self.conta.sacar(40.0)
        self.assertEqual(self.conta.saldo, 60.0)

    def test_sacar_maior_que_saldo_lanca_erro(self):
        with self.assertRaises(ValueError):
            self.conta.sacar(200.0)
    
    def test_depositar_valor_invalido_lanca_erro(self):
        for invalido in [0, -10]:
            with self.subTest(valor=invalido):
                with self.assertRaises(ValueError):
                    self.conta.depositar(invalido)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)