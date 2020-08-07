#!/usr/bin/python3
"""
Unitests to amenity.py
"""

import unittest
import models
from models.amenity import Amenity
from models.base_model import BaseModel


class amenity_tests1(unittest.TestCase):
    """Assert tests"""

    def test_subclass(self):
        """amenity is a subclass"""
        inst = Amenity()
        self.assertIsInstance(inst, BaseModel)
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

    def test_output(self):
        """show if the output works"""
        inst = Amenity()
        out = "[Amenity] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(out, str(inst))

    def test_name(self):
        """test name exists in amenity instance"""
        inst = Amenity()
        self.assertTrue(hasattr(inst, "name"))
        self.assertEqual(inst.name, "")
