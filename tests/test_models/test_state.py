#!/usr/bin/python3
"""
Unitests to state.py
"""

import unittest
import models
from models.state import State
from models.base_model import BaseModel


class state_tests1(unittest.TestCase):
    """Assert tests"""

    def test_subclass(self):
        """State is a subclass"""
        inst = State()
        self.assertIsInstance(inst, BaseModel)
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

    def test_output(self):
        """show if the output works"""
        inst = State()
        out = "[State] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(out, str(inst))

    def test_name(self):
        """test parameters exists in State instance"""
        inst = State()
        self.assertTrue(hasattr(inst, "name"))
        self.assertEqual(inst.name, "")
