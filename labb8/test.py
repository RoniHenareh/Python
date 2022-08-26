
# eget testprogramm med unitest

import unittest

from syntax import *

class SyntaxTest(unittest.TestCase):

    def testa_rätt_syntax(self):
        """ Testar molekyler """
        self.assertEqual(testar("H2"), 'Formen är syntastiskt korrekt')

    def testar_fel_syntax(self):
        self.assertEqual(testar("a"), 'Saknad stor bokstav vid radslutet a')

if __name__ == '__main__':
    unittest.main()
