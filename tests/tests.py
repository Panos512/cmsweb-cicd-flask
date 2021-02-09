# project/test_basic.py
 
import os
import unittest 
 
 
class BasicTests(unittest.TestCase):

    def test_main_page(self):
        self.assertEqual(400, 200)
 
 
if __name__ == "__main__":
    unittest.main()