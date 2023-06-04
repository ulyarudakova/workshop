import unittest
import random


class TestRandomNumbers(unittest.TestCase):

    def test_random_numbers(self):
        n = 10
        for i in range(n):
            rand_num = random.uniform(0, 1)
            with self.subTest(i=i, rand_num=rand_num):
                self.assertGreaterEqual(rand_num, 0.5)


if __name__ == '__main__':
    unittest.main()
