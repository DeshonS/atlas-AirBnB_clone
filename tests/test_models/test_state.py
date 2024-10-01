#!/usr/bin/python3
"""State class tester"""
from models.state import State
from models.base_model import BaseModel
import unittest


class TestState(unittest.TestCase):
    """Test State class"""

    def setUp(self):
        self.State = State()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.State, State))
        
    def test_name_init(self):
        self.assertEqual(self.State.name, "")
        
    def test_name_type(self):
        self.assertTrue(hasattr(self.State, "name"))
        
if __name__ == "__main__":
    unittest.main()