import unittest
from decimal import Decimal as D
from tom_calc import amount, discount, tax, \
    discounted_amount, discounted_taxed_amount, \
    calculate


class TestTomCalc(unittest.TestCase):

    def test_amount(self):
        self.assertEqual(amount(0, 0), D('0'))
        self.assertEqual(amount(0.0, 0), D('0'))
        self.assertEqual(amount(0, 0.0), D('0'))
        self.assertEqual(amount(0.0, 0.0), D('0'))
        self.assertEqual(amount(1.33, 7.66), D('10.19'))
        with self.assertRaises(TypeError):
            amount('', '')

    def test_discount(self):
        self.assertEqual(discount(D('0')), D('0'))
        self.assertEqual(discount(D('1000')), D('3'))
        self.assertEqual(discount(D('5000')), D('5'))
        self.assertEqual(discount(D('7000')), D('7'))
        self.assertEqual(discount(D('10000')), D('10'))
        self.assertEqual(discount(D('50000')), D('15'))
        self.assertEqual(discount(D('100000')), D('15'))
        self.assertEqual(discount(D('0.0')), D('0'))
        self.assertEqual(discount(D('999')), D('0'))
        self.assertEqual(discount(D('999.99')), D('0'))
        self.assertEqual(discount(D('1000.00')), D('3'))

    def test_tax(self):
        self.assertEqual(tax('UT'), D('6.85'))
        self.assertEqual(tax('NV'), D('8'))
        self.assertEqual(tax('TX'), D('6.28'))
        self.assertEqual(tax('AL'), D('4'))
        self.assertEqual(tax('CA'), D('8.25'))
        with self.assertRaises(KeyError):
            tax('AB')
            tax('')

    def test_discounted_amount(self):
        self.assertEqual(discounted_amount(D('0')), D('0'))
        self.assertEqual(discounted_amount(D('1')), D('1'))
        self.assertEqual(discounted_amount(D('999')), D('999'))
        self.assertEqual(discounted_amount(D('999.99')), D('999.99'))
        self.assertEqual(discounted_amount(D('1000')), D('970'))
        self.assertEqual(discounted_amount(D('1000.00')), D('970'))

    def test_discounted_taxed_amount(self):
        self.assertEqual(discounted_taxed_amount(D('0'), 'TX'), D('0'))
        self.assertEqual(discounted_taxed_amount(D('1'), 'TX'), D('1.06'))
        self.assertEqual(discounted_taxed_amount(
            D('1000'), 'TX'), D('1030.92'))

    def test_calculate(self):
        self.assertEqual(calculate(0, 0, 'TX'), D('0'))
        self.assertEqual(calculate(20, 30.33, 'TX'), D('644.69'))
        self.assertEqual(calculate(20, 50, 'TX'), D('1030.92'))
