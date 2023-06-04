import unittest


def subtract(a, b):
    c = a - b
    return c


def subtract1(a, b):
    c = a + b
    return c


def subtract2(a, b):
    c = a - b
    return c > a


def subtract3(a, b):
    c = a + b
    return c < a


def subtract4(a):
    b = list(a)
    return b


def subtract5(a):
    b = a.split()
    return b


def subtract6(a):
    b = a ** 2
    return b


class TestFunctions(unittest.TestCase):
    def test_greater_1(self):
        self.assertGreater(subtract(4, 2), 1)

    def test_greater_2(self):
        self.assertGreater(subtract(4, 2), 4)

    def test_less_1(self):
        self.assertLess(subtract1(6, 2), 9)

    def test_less_2(self):
        self.assertLess(subtract1(6, 2), 5)

    def test_true_1(self):
        self.assertTrue(subtract2(5, -2))

    def test_true_2(self):
        self.assertTrue(subtract2(5, 2))

    def test_false_1(self):
        self.assertFalse(subtract3(3, 1))

    def test_false_2(self):
        self.assertFalse(subtract3(-4, -1))

    def test_count_1(self):
        self.assertCountEqual(subtract4("май"), subtract4("йам"))

    def test_count_2(self):
        self.assertCountEqual(subtract4("закат"), subtract4("рассвет"))

    def test_in_1(self):
        self.assertIn("вечер", subtract5("вечер перестаёт быть томным"))

    def test_in_2(self):
        self.assertIn("взрослые", subtract5("во дворе играют дети"))

    def test_not_in_1(self):
        self.assertNotIn(subtract6(5), [4, 6, 8])

    def test_not_in_2(self):
        self.assertNotIn(subtract6(2), [4, 6, 8])


if __name__ == '__main__':
    unittest.main()
