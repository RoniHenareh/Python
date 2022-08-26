import unittest

from syntax import *

class Test(unittest.TestCase):

    def test1_korrekt(self):
        self.assertEqual(testar('Na'), 'Formeln är syntaktiskt korrekt')

    def test2_korrekt(self):
        self.assertEqual(testar('H2O'), 'Formeln är syntaktiskt korrekt')

    def test3_korrekt(self):
        self.assertEqual(testar('Si(C3(COOH)2)4(H2O)7'), 'Formeln är syntaktiskt korrekt')

    def test4_korrekt(self):
        self.assertEqual(testar('Na332'), 'Formeln är syntaktiskt korrekt')

    def test5_okänd(self):
        self.assertEqual(testar('C(Xx4)5'), 'Okänd atom vid radslutet 4)5')

    def test6_saknad_siffra(self):
        self.assertEqual(testar('C(OH4)C'), 'Saknad siffra vid radslutet C')

    def test7_saknad_parantes(self):
        self.assertEqual(testar('C(OH4C'), 'Saknad högerparentes vid radslutet')

    def test8_fel_gruppstart(self):
        self.assertEqual(testar('H2O)Fe'), 'Felaktig gruppstart vid radslutet )Fe')

    def test9_litet_tal(self):
        self.assertEqual(testar('H0'), 'För litet tal vid radslutet ')

    def test10_litet_tal(self):
        self.assertEqual(testar('H1C'), 'För litet tal vid radslutet C')

    def test11_litet_tal(self):
        self.assertEqual(testar('H02C'), 'För litet tal vid radslutet 2C')

    def test12_saknad_stor(self):
        self.assertEqual(testar('Nacl'), 'Saknad stor bokstav vid radslutet cl')

    def test13_saknad_stor(self):
        self.assertEqual(testar('a'), 'Saknad stor bokstav vid radslutet a')

    def test14_fel_grupp(self):
        self.assertEqual(testar('(Cl)2)3'), 'Felaktig gruppstart vid radslutet )3')

    def test15_fel_grupp(self):
        self.assertEqual(testar(')'), 'Felaktig gruppstart vid radslutet )')

    def test16_fel_grupp(self):
        self.assertEqual(testar('2'), 'Felaktig gruppstart vid radslutet 2')

    def test18_tom_parentes(self):
        self.assertEqual(testar('()'), 'Felaktig gruppstart vid radslutet )')

    def test19_massa_parenteser_korrekt(self):
        self.assertEqual(testar('(C(H(H2O)2)4)99'), 'Formeln är syntaktiskt korrekt')

    def test21_massa_parenteser_saknad_siffra(self):
        self.assertEqual(testar('(O(H(H2O)2)4)'), 'Saknad siffra vid radslutet ')


if __name__ == "__main__":
    unittest.main()