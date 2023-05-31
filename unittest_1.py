import unittest


def subtract(a, b):
    c = a - b
    return c < a


def check_list(lst, item):
    return item in lst


def check_greater(a, b):
    return a > b


def check_less(a, b):
    return a < b


def check_count(lst, items):
    return lst.count(items[0]) == items.count(items[0]) and lst.count(items[1]) == items.count(items[1])


class TestFunctions(unittest.TestCase):
    def test_subtract(self):
        self.assertTrue(subtract(10, 3))
        self.assertFalse(subtract(-5, -3))

    def test_check_list(self):
        lst = [1, 2, 3, 4]
        self.assertIn(2, lst)
        self.assertNotIn(5, lst)

    def test_check_greater(self):
        self.assertGreater(10, 5)

    def test_check_less(self):
        self.assertLess(5, 10)

    def test_check_count(self):
        lst = [1, 2, 3, 4, 2, 3]
        self.assertCountEqual(lst, [1, 2, 2, 3, 3, 4])


if __name__ == '__main__':
    unittest.main()
