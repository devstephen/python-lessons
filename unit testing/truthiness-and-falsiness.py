import unittest


class TruthyAndFalsy(unittest.TestCase):
    def test_truthiness(self):
        # self.assertEqual( 3 < 5, True )
        self.assertTrue( 3 < 5)
        self.assertTrue("hello")
        self.assertTrue("a")

        def test_falsiness(self):
            self.assertFalse(False)
            self.assertFalse(0)
            self.assertFalse("")


if __name__ == "__main__":
    unittest.main()