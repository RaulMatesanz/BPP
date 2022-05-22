import unittest
import Pruebas
import pandas as pd

csv = pd.read_csv("C:/Users/Raul/Desktop/Master/Buenas_Prácticas_de_Programacion_en_Python/Tema1/Práctica/finanza.csv"
,engine="python", thousands='.', decimal=',', sep='\t')
maximo=csv.max()

class PruebasUnit(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(Pruebas.suma(18,2), 20)
    def test_media(self):
        self.assertEqual(Pruebas.CalculaMedia(2,4,6,8,10), 6)
    def test_Mayus(self):
        self.assertTrue(Pruebas.Mayus("compra".upper(), "COMPRA"))
    def test_espacio(self):
        frase = "Buenos días"
        self.assertEqual(frase.split(), ["Buenos", "días"])
        with self.assertRaises(TypeError):
            frase.split(2)
    def test_meses(self):
        self.assertTrue(Pruebas.meses(len(maximo),11))
    def test_palabra(self):
        self.assertGreater(Pruebas.longitud(len("buenos dias"),
        len("Hola")),len("adios"))


if __name__ == "__main__":
    unittest.main()
