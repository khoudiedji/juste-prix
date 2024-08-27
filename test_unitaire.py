import unittest
import juste_prix
class Test(unittest.TestCase):
    #def test_juste_prix(self):
     #   juste_prix.juste_prix()
    def test_trouve(self):
        self.assertEqual(juste_prix.verif(5,4), "Bonne réponse")