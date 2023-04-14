import unittest
from fibonacci import fibonacciiter

class test_numeracion(unittest.TestCase):
    def test_fibonacci(self):
        resp = fibonacciiter(5)
        self.assertEqual(resp, [0,1,1,2,3])


if __name__ == "__main__":
    unittest.main()
