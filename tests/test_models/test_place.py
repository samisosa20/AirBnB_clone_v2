#!/usr/bin/python3
"""
Unitests to place.py
"""

import unittest
import models
from models.place import Place
from models.base_model import BaseModel


class place_tests1(unittest.TestCase):
    """Assert tests"""

    def test_subclass(self):
        """Place is a subclass"""
        inst = Place()
        self.assertIsInstance(inst, BaseModel)
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

    def test_output(self):
        """show if the output works"""
        inst = Place()
        out = "[Place] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(out, str(inst))

    def test_name(self):
        """test name exists in Place instance"""
        inst = Place()
        self.assertTrue(hasattr(inst, "city_id"))
        self.assertEqual(inst.city_id, "")
        self.assertTrue(hasattr(inst, "user_id"))
        self.assertEqual(inst.user_id, "")
        self.assertTrue(hasattr(inst, "name"))
        self.assertEqual(inst.name, "")
        self.assertTrue(hasattr(inst, "description"))
        self.assertEqual(inst.description, "")
        self.assertTrue(hasattr(inst, "number_rooms"))
        self.assertEqual(inst.number_rooms, 0)
        self.assertTrue(hasattr(inst, "number_bathrooms"))
        self.assertEqual(inst.number_bathrooms, 0)
        self.assertTrue(hasattr(inst, "max_guest"))
        self.assertEqual(inst.max_guest, 0)
        self.assertTrue(hasattr(inst, "price_by_night"))
        self.assertEqual(inst.price_by_night, 0)
        self.assertTrue(hasattr(inst, "latitude"))
        self.assertEqual(inst.price_by_night, 0.0)
        self.assertTrue(hasattr(inst, "longitude"))
        self.assertEqual(inst.longitude, 0.0)
        self.assertTrue(hasattr(inst, "amenity_ids"))
        self.assertEqual(inst.amenity_ids, [])
