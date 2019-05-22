import unittest
import challenge2
class TestProblemTwo(unittest.TestCase):

    def test_new_array(self):
        self.assertEqual(challenge2.new_array([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
        self.assertEqual(challenge2.new_array([3, 2, 1]), [2, 3, 6])
        self.assertEqual(challenge2.new_array([2, 5, 8, 5]), [200, 80, 50, 80])
        self.assertEqual(challenge2.new_array([2, 2, 3, 2]), [12, 12, 8, 12])
        self.assertEqual(challenge2.new_array([8, 2, 2, 4]), [16, 64, 64, 32])



    if __name__ == '__main__':
        unittest.main()
