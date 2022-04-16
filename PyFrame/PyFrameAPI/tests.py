from django.test import TestCase
from PyService.basic import Basic

# Create your tests here.
class BasicTestCase(TestCase):
    def test_simple_add_calcul(self):
        self.assertEqual(Basic("1+1"), 1 + 1)
        
    def test_simple_add_2_calcul(self):
        self.assertEqual(Basic("2+1+4"), 2 + 1 + 4)

    def test_simple_add_3_calcul(self):
        self.assertEqual(Basic("5+4"), 5+4)

    def test_simple_add_4_calcul(self):
        self.assertEqual(Basic("2+1023+4"), 2 + 1023 + 4)

    def test_simple_mul_calcul(self):
        self.assertEqual(Basic("4*2"), 4 * 2)

    def test_simple_mul_2_calcul(self):
        self.assertEqual(Basic("8*2"), 8 * 2)

    def test_simple_div_calcul(self):
        self.assertEqual(Basic("8/2"), 8 / 2)
        
    def test_simple_pow_calcul(self):
        self.assertEqual(Basic("8^2"), pow(8, 2))

    def test_mul_parenthesis_calcul(self):
        self.assertEqual(Basic("1*(2+3)"), 1 * (2 + 3))

    def test_div_parenthesis_calcul(self):
        self.assertEqual(Basic("1/(2*4)"), 1 / (2 * 4))

    def test_mul_add_div_calcul(self):
        self.assertEqual(Basic("2*8+3/2+1"), 2 * 8 + 3 / 2 + 1)

    def test_float_mul_calcul(self):
        self.assertEqual(Basic("101.2*3"), 101.2 * 3)

    def test_complex_mix_1_calcul(self):
        self.assertEqual(Basic("45.87*37.17/74.23*(12/2*3)"), 45.87 * 37.17 / 74.23 * (12 / 2 * 3))

    def test_pow_mix_calcul(self):
        self.assertEqual(Basic("8^3*2*(2/1)"), pow(8, 3) * 2 * (2 / 1))
        
    def test_complex_mix_2_calcul(self):
        self.assertEqual(Basic("8.1/2.3*3+(1-3.23)"), 8.1 / 2.3 * 3 + (1 - 3.23))

    def test_complex_mix_3_calcul(self):
        self.assertEqual(Basic("8.12/4*3+(2/4.0+102)/2+6*2"), 8.12 / 4 * 3 + (2 / 4.0 + 102) / 2 + 6 * 2)