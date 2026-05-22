import unittest


class TestesCalculadora(unittest.TestCase):

    def test_funcao_soma_simples(self):
     

        resultado = somar_numeros(2, 3)
        self.assertEqual(resultado, 5)


    def test_classe_calculadora_soma(self):
        calc = Calculadora()
 

        self.assertEqual(calc.somar(10, 5), 15)
        self.assertEqual(calc.somar(-1, 1), 0)

    def test_classe_calculadora_divisao(self):
  
        self.assertEqual(calc.dividir(10, 2), 5)
        self.assertEqual(calc.dividir(5, 2), 2.5)


    def test_divisao_por_zero_deve_dar_erro(self):
        calc = Calculadora()

    
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)


if __name__ == "__main__":
    unittest.main()
