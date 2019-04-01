import unittest
from transform import Transform

class TestTransformMethods(unittest.TestCase):
    t = Transform()

    def test_is_palindrome(self):
        self.assertEqual(self.t.is_palindrome(121), True)
        self.assertEqual(self.t.is_palindrome(11111),True)
        self.assertEqual(self.t.is_palindrome(34543), True)
        self.assertEqual(self.t.is_palindrome(3443), True)
        self.assertEqual(self.t.is_palindrome(3434), False)
        self.assertEqual(self.t.is_palindrome(1000), False)

    def test_palindrome(self):
        self.assertEqual(self.t.palindrome(28), 121)
        self.assertEqual(self.t.palindrome(51), 66)
        self.assertEqual(self.t.palindrome(11), 11)
        self.assertEqual(self.t.palindrome(607), 4444)
        self.assertEqual(self.t.palindrome(196), -1)
    
    def test_palindrome_w_cycles(self):
        self.assertEqual(self.t.palindrome_w_cycles(28), (121, 2))
        self.assertEqual(self.t.palindrome_w_cycles(51), (66, 1))
        self.assertEqual(self.t.palindrome_w_cycles(11111), (11111, 0))

if __name__ == '__main__':
    unittest.main()