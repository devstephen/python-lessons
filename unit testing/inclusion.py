import unittest

class InclusionTests(unittest.TestCase):
    def test_inclusion(self):
       
        # self.assertTrue("k" in "king")
        self.assertIn("k", "king")
        self.assertIn(1, [1,2,3])
        self.assertIn(5, (6, 5,7))
        self.assertIn("a", {"a":1, "b":2, "c":3}.keys() )
        self.assertIn(2, {"a":1, "b":2, "c":3}.values() )
        self.assertIn(55, range(0, 75))

    def test_none_inclusion(self):
        self.assertNotIn("w", "king")
        self.assertNotIn(10, [24, 27, 12])
    

if __name__ == "__main__":
    unittest.main()


