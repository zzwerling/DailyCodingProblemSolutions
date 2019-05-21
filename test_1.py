import unittest
import challenge1
class TestProblemOne(unittest.TestCase):

    def test_adds_up(self):
        self.assertTrue(challenge1.adds_up([10, 15, 3, 7], 17))
        self.assertTrue(challenge1.adds_up([4, 5, 2, 19], 21))
        self.assertTrue(challenge1.adds_up([5, 8, 16, 12], 24))
        self.assertTrue(challenge1.adds_up([4, 3, 9, 1], 4))

        self.assertFalse(challenge1.adds_up([12, 16, 3, 1], 18))
        self.assertFalse(challenge1.adds_up([6, 5, 15, 19], 22))
        self.assertFalse(challenge1.adds_up([5, 23, 16, 12], 24))
        self.assertFalse(challenge1.adds_up([4, 6, 9, 1], 11))

    if __name__ == '__main__':
        unittest.main()
