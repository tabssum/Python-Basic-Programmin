import unittest
class Test_String(unittest.TestCase):
    def test_stringEqual(self):
        self.assertEqual('FOO','FOO')

    def test_stringUpper(self):
        self.assertTrue('FOo'.isupper())

    

if __name__=='__main__':
    unittest.main()
