import unittest
import rpn

class TestBasics(unittest.TestCase):
  def test_add(self):
    result = rpn.calculate('1 1 +')
    self.assertEqual(2, result)

  def test_subtract(self):
    result = rpn.calculate('4 3 -')
    self.assertEqual(1, result)

  def test_multiply(self):
    result = rpn.calculate('4 3 *')
    self.assertEqual(12, result)

  def test_exponent(self):
    result = rpn.calculate('2 3 ^')
    self.assertEqual(8, result)

  def test_factorial(self):
    result = rpn.calculate('4 !')
    self.assertEqual(24, result)

  def test_and(self):
    result = rpn.calculate('1 1 &')
    self.assertEqual(1, result)

  def test_or(self):
    result = rpn.calculate('1 0 |')
    self.assertEqual(1, result)
    
  def test_not(self):
    result = rpn.calculate('1 ~')
    self.assertEqual(-2, result)
    
  def test_ptC(self):
    result = rpn.calculate('3 4 ptC')
    self.assertEqual(5, result)

  def test_ptA(self):
    result = rpn.calculate('5 4 ptA')
    self.assertEqual(3, result)

  def test_ptB(self):
    result = rpn.calculate('5 4 ptB')
    self.assertEqual(3, result)

  def test_toomany(self):
    with self.assertRaises(ValueError):
      result = rpn.calculate('1 2 3 +')