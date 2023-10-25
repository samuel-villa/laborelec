import unittest
from laborelec import longestRun

class TestLongestRunFunction(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(longestRun(""), 0)

    def test_single_character(self):
        self.assertEqual(longestRun("a"), 1)

    def test_multiple_characters(self):
        self.assertEqual(longestRun("abcd"), 1)
        self.assertEqual(longestRun("abcaaad"), 3)
        self.assertEqual(longestRun("a simple string with aaaabbbcccdddd"), 4)

    def test_symbols(self):
        self.assertEqual(longestRun(":"), 1)
        self.assertEqual(longestRun(":::"), 3)
        self.assertEqual(longestRun(": ababa,,   ))))"), 4)


if __name__ == '__main__':
    unittest.main()
