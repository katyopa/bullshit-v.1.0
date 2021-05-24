import unittest
import functions as fc
import tagcounter as tc
import argparse


class Test(unittest.TestCase):
    def test_add_protocol_to_url(self):
        self.assertEqual(fc.add_protocol_to_url("google.com"), "http://google.com")

    def test_parse_tagcounter_args(self):
        self.assertIsInstance(tc.parse_tagcounter_args(), argparse.Namespace)

    def test_parse_yaml_file(self):
        self.assertIsInstance(fc.parse_yaml_file(), dict)


if __name__ == "__main__":
    unittest.main()
