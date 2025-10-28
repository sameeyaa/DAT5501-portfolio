#simple addition unit test

import unittest
from week_2 import add

class test(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()

print("unit test successful")
