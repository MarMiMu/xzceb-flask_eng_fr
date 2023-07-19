import unittest
from translator import english_to_french
from translator import french_to_english

class TestMethods(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(english_to_french("Bye"),"Bonjour")
    def test_f2e(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(english_to_french("Bonjour"),"Bye")

if __name__ == '__main__':
    unittest.main()
