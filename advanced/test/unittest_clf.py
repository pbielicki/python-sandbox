import unittest
from clf import fib

class Fib(unittest.TestCase):
    
    def test_fib(self):
        self.assertEqual(0, fib(0))
        
if __name__ == "__main__":
    unittest.main()