#!/usr/bin/python3
"""
Unitests to review.py
"""

import unittest
import models
from models.review import Review
from models.base_model import BaseModel


class review_tests1(unittest.TestCase):
    """Assert tests"""

    def test_subclass(self):
        """Review is a subclass"""
        inst = Review()
        self.assertIsInstance(inst, BaseModel)
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

    def test_output(self):
        """show if the output works"""
        inst = Review()
        out = "[Review] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(out, str(inst))

    def test_name(self):
        """test name exists in Review instance"""
        inst = Review()
        self.assertTrue(hasattr(inst, "place_id"))
        self.assertEqual(inst.place_id, "")
        self.assertTrue(hasattr(inst, "user_id"))
        self.assertEqual(inst.user_id, "")
        self.assertTrue(hasattr(inst, "text"))
        self.assertEqual(inst.user_id, "")
