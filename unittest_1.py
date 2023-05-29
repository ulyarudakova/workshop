import unittest


class FunctionsTest(unittest.TestCase):
    def test_is_even(self):
        num = 2
        self.assertTrue(num % 2 == 0)

    def test_is_odd(self):
        num = 3
        self.assertFalse(num % 2 == 0)

    def test_is_in_list(self):
        my_list = [1, 2, 3, 4]
        self.assertIn(3, my_list)

    def test_is_not_in_list(self):
        my_list = [1, 2, 3, 4]
        self.assertNotIn(5, my_list)

    def test_is_greater_than(self):
        num1 = 5
        num2 = 3
        self.assertGreater(num1, num2)

    def test_is_less_than(self):
        num1 = 3
        num2 = 5
        self.assertLess(num1, num2)

    def test_count_equal(self):
        list1 = [1, 2, 3]
        list2 = [3, 2, 1]
        self.assertCountEqual(list1, list2)


if __name__ == '__main__':
    unittest.main()
