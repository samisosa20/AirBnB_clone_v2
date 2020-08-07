#!/usr/bin/python3
"""
unittest to city.py
"""


import unittest
import models
from models.city import City
from models.base_model import BaseModel


class city_test1(unittest.TestCase):
    """Assert cases to City"""

    def test_subclass(self):
        """City is a subclass"""
        inst = City()
        self.assertIsInstance(inst, BaseModel)
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

    def test_output(self):
        """show if the output works"""
        inst = City()
        out = "[City] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(out, str(inst))

    def test_name(self):
        """test name exists in amenity instance"""
        inst = City()
        self.assertTrue(hasattr(inst, "name"))
        self.assertEqual(inst.name, "")
        self.assertTrue(hasattr(inst, "state_id"))
        self.assertEqual(inst.state_id, "")
