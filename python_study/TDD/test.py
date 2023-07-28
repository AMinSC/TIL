import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
    
    def test_add(self):
        self.assertEqual(1 + 2, 3)
    
    def test_add(self):
        self.assertTrue(10 == 10)

    def test_add(self):
        self.assertFalse(1 == 10)

    def test_add(self):
        self.assertGreater(10, 1)
    
    def test_add(self):
        self.assertLess(1, 10)
    
    def test_add(self):
        self.assertIn(1, [1, 2, 3, 4, 5])
    
    def test_add(self):
        self.assertIsInstance('a', str)

if __name__ == '__main__':
    unittest.main()