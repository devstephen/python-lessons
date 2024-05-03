import unittest

def copy_and_add_element(values, element):
    copy = values[:]
    copy.append(element)
    return copy

class TestInequality(unittest.TestCase):
    def  test_inequality(self):
        self.assertNotEqual(1, 2)
        self.assertNotEqual(True, False)
        self.assertNotEqual("Hello", "hello")

    def test_copy_and_add_element(self):
        values = [1, 2, 3]
        result = copy_and_add_element(values, 4)
        

        self.assertEqual(result, [1, 2, 3, 4])
        self.assertNotEqual(values, result, "Make sure to create a copy. Original list is mutated")


if __name__ == "__main__":
    unittest.main()