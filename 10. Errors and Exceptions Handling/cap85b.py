import cap85a
import unittest

class Test(unittest.TestCase):

    def test_1(self):
        texto = 'python'
        resultado = cap85a.prueba(texto)
        self.assertEqual(resultado,'Python')

if __name__ == '__main__':
    unittest.main()