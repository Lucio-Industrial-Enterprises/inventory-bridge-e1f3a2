import unittest

from warehouse.quantity import parse_quantity


class QuantityTests(unittest.TestCase):
    def test_valid_positive(self):
        self.assertEqual(parse_quantity("42"), 42)

    def test_whitespace_stripped(self):
        self.assertEqual(parse_quantity("  7  "), 7)

    # Regression: zero should be accepted (boundary value)
    def test_zero_accepted(self):
        self.assertEqual(parse_quantity("0"), 0)

    # Regression: negative quantities must be rejected
    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("-1")

    def test_large_negative_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("-999")
