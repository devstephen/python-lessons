import unittest

class ObjectTypeTests(unittest.TestCase):
    def test_is_instance(self):
        self.assertIsInstance(2, int)
        self.assertIsInstance(3.142, float)
        self.assertIsInstance("Rob", str)
        self.assertIsInstance(["Rob"], list)
        self.assertIsInstance({}, dict)


    def test_not_is_instance(self):
        self.assertNotIsInstance("", int)
        self.assertNotIsInstance(3.142, int)
        self.assertNotIsInstance("Rob", list)
        self.assertNotIsInstance(["Rob"], dict)
        self.assertNotIsInstance({}, list)
if __name__ == "__main__":
    unittest.main()