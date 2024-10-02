#!/usr/bin/python3
"""Unittest for city.py"""
from models.city import City
from models.base_model import BaseModel
import unittest


class TestCity(unittest.TestCase):
    """Tests instances and methods from City class"""

    def setUp(self):
        self.city = City()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.city, City))
        
    def test_init(self):
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")
        
    def test_name_type(self):
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))
        
        
if __name__ == "__main__":
    unittest.main()