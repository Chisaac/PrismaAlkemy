import unittest
from funciones import add
from funciones import substract
from funciones import multiply
from funciones import divide


class calculator(unittest.TestCase):
    def test_add(self,number1,number2):
        self.assertEqual(add(number1,number2),number1+number2)
    def test_substract(self,number1,number2):
        self.assertEqual(substract(number1,number2),number1-number2)
    def test_multiply(self,number1,number2):
        self.assertEqual(multiply(number1,number2),number1*number2)
    def test_divide(self,number1,number2):
        self.assertEqual(divide(number1,number2),number1/number2)

if __name__ == '__main__':
    unittest.main()