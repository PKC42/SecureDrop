import unittest
from utilities import *
from communications import *

class TestStringMethods(unittest.TestCase):
    def test_file_scan(self):
        self.assertTrue(user_file_scan())

    def test_get_timestamp(self):
        self.assertTrue(get_timestamp("contacts.json"))

    def broadcast_test(self):
        broadcast()
   
if __name__ == '__main__':
    unittest.main()