import  unittest

class TestSkipping(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)
        
    def test_subtract(self):    
        self.assertEqual(3 - 1, 2)

    @unittest.skip("Todo")
    def test_multiplication(self):
        pass



if __name__ == "__main__":
    unittest.main()