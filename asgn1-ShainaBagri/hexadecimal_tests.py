# Tests operations on hexadecimal numbers.
# CSC 225, Assignment 1
# Given tests, Winter '20

import unittest
import hexadecimal as hx

class TestHexadecimal(unittest.TestCase):
    def test01_binary_to_hex(self):
        msg = "Testing basic binary-to-hex conversion"
        self.assertEqual(hx.binary_to_hex("0000010100011010"), "0x051A", msg)

    def test02_binary_to_hex(self):
        msg = "Testing basic binary-to-hex conversion"
        self.assertEqual(hx.binary_to_hex("1001010100001011"), "0x950B", msg)

    def test03_hex_to_binary(self):
        msg = "Testing basic hex-to-binary conversion"
        self.assertEqual(hx.hex_to_binary("0x051A"), "0000010100011010", msg)

    def test04_hex_to_binary(self):
        msg = "Testing basic hex-to-binary conversion"
        self.assertEqual(hx.hex_to_binary("0x950B"), "1001010100001011", msg)


if __name__ == "__main__":
    unittest.main()
