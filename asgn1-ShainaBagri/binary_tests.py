# Tests operations on binary numbers.
# CSC 225, Assignment 1
# Given tests, Winter '20

import unittest
import binary as bn

class TestBinary(unittest.TestCase):
    def test01_add(self):
        msg = "Testing basic binary addition"
        self.assertEqual(bn.add("00000011", "00000010"), "00000101", msg)

    def test02_add(self):
        msg = "Testing basic binary addition"
        self.assertEqual(bn.add("00100110", "00000111"), "00101101", msg)

    def test03_negate(self):
        msg = "Testing basic binary negation"
        self.assertEqual(bn.negate("00000001"), "11111111", msg)

    def test04_negate(self):
        msg = "Testing basic binary negation"
        self.assertEqual(bn.negate("01111111"), "10000001", msg)

    def test05_subtract(self):
        msg = "Testing basic binary subtraction"
        self.assertEqual(bn.subtract("00000011", "00000010"), "00000001", msg)

    def test06_subtract(self):
        msg = "Testing basic binary subtraction"
        self.assertEqual(bn.subtract(bn.negate("00000001"), "00000001"), bn.negate("00000010"), msg)

    def test07_subtract(self):
        msg = "Testing basic binary subtraction"
        self.assertEqual(bn.subtract("00000110", "00000101"), "00000001", msg)

    def test08_binary_to_decimal(self):
        msg = "Testing basic binary-to-decimal conversion"
        self.assertEqual(bn.binary_to_decimal("00000101"), 5, msg)

    def test09_binary_to_decimal(self):
        msg = "Testing basic binary-to-decimal conversion"
        self.assertEqual(bn.binary_to_decimal("10000001"), -127, msg)

    def test10_binary_to_decimal(self):
        msg = "Testing basic binary-to-decimal conversion"
        self.assertEqual(bn.binary_to_decimal("10000000"), -128, msg)

    def test11_binary_to_decimal(self):
        msg = "Testing basic binary-to-decimal conversion"
        self.assertEqual(bn.binary_to_decimal("01111111"), 127, msg)

    def test12_decimal_to_binary(self):
        msg = "Testing basic decimal-to-binary conversion"
        self.assertEqual(bn.decimal_to_binary(5), "00000101", msg)

    def test13_decimal_to_binary(self):
        msg = "Testing basic decimal-to-binary conversion"
        self.assertEqual(bn.decimal_to_binary(-127), "10000001", msg)

    def test14_decimal_to_binary(self):
        msg = "Testing basic decimal-to-binary conversion"
        self.assertEqual(bn.decimal_to_binary(127), "01111111", msg)

    def test15_decimal_to_binary(self):
        msg = "Testing basic decimal-to-binary conversion"
        self.assertEqual(bn.decimal_to_binary(-128), "10000000", msg)

    def test16_decimal_to_binary(self):
        msg = "Testing basic decimal-to-binary conversion"
        with self.assertRaises(OverflowError):
            bn.decimal_to_binary(128)


if __name__ == "__main__":
    unittest.main()
