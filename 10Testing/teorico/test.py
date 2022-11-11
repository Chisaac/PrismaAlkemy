import unittest
from unittest import TestCase

class TestStringMethods(unittest,TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')
    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    def test_split(self):
        s = 'helo world'
        self.assertEqual(s.split(),['hello','world'])
        #check that s.split fails when te separator is not a string
        with self.assetRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main