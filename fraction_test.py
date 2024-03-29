import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        f = Fraction(0,0)
        self.assertEqual("0/0", f.__str__())
        f = Fraction(-1,0)
        self.assertEqual("-1/0", f.__str__())

    def test_invalid_numerator_fraction(self):
        # If initialize the fraction with non-int or non-float will raise exception
        with self.assertRaises(TypeError):
            Fraction('str', 3)

    def test_invalid_denominator_fraction(self):
        # If initialize the fraction with non-int or non-float will raise exception
        with self.assertRaises(TypeError):
            Fraction(3, 'str')

    # TODO Write tests for __init__, __eq__, +, *.
    # Here is an example, but you must add more test cases.  
    # The test requires that your __eq__ is correct.
    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        self.assertEqual(Fraction(9,4), Fraction(2)+Fraction(1,4))
        self.assertEqual(Fraction(2), Fraction(1,2)+Fraction(3,2))
        self.assertEqual(Fraction(9,8), Fraction(0)+Fraction(9,8))
        self.assertEqual(Fraction(-16,8), Fraction(-7,8)+Fraction(-9,8))
        self.assertEqual(Fraction(1,0), Fraction(1,0)+Fraction(5,6))
        self.assertEqual(Fraction(0,0), Fraction(0,0)+Fraction(5,6))
    
    def test_mul(self):
        # 2/36 = 1/12 * 2/3
        self.assertEqual(Fraction(2,36), Fraction(1,12) * Fraction(2,3))
        self.assertEqual(Fraction(1), Fraction(4) * Fraction(3,12))
        self.assertEqual(Fraction(0), Fraction(0) * Fraction(500,-20000))
    
    def test_sub(self):
        # -7/12 = 1/12 - 2/3
        self.assertEqual(Fraction(-7,12), Fraction(1,12) - Fraction(2,3))
        self.assertEqual(Fraction(7,4), Fraction(2) - Fraction(1,4))
        

    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        self.assertTrue(Fraction(1,0) == Fraction(9999999,0)) # Check if denominator = 0
        self.assertTrue(Fraction(-1,0) == Fraction(-9999999,0)) # Check if denominator = 0
        #TODO write more tests using other cases.
        # Consider special values like 0, 1/0, -1/0
        self.assertFalse(Fraction(0) == Fraction(1,0))
        self.assertFalse(Fraction(-1,0) == Fraction(1,0))
        self.assertTrue(Fraction(3,4) == Fraction(-9,-12))

    def test_gt(self):
        # 2/3 > 5/12 True
        f = Fraction(2,3)
        g = Fraction(5,12)
        self.assertTrue(f.__gt__(g))
        self.assertFalse(g.__gt__(f))

    def test_neg(self):
        # -3/4 is 3/4
        self.assertEqual(Fraction(-3,4), -Fraction(3,4))
        self.assertEqual(Fraction(3,4), -Fraction(3,-4))
        self.assertEqual(Fraction(-99), -Fraction(99))
        self.assertEqual(Fraction(0), -Fraction(0))
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
