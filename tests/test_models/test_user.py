#!/usr/bin/python3
"""
Unitests to user.py
"""

import unittest
import models
from models.user import User
from models.base_model import BaseModel


class review_tests1(unittest.TestCase):
    """Assert tests"""

    def test_subclass(self):
        """User is a subclass"""
        inst = User()
        self.assertIsInstance(inst, BaseModel)
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

    def test_output(self):
        """show if the output works"""
        inst = User()
        out = "[User] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(out, str(inst))

    def test_name(self):
        """test parameters exists in User instance"""
        inst = User()
        self.assertTrue(hasattr(inst, "email"))
        self.assertEqual(inst.email, "")
        self.assertTrue(hasattr(inst, "password"))
        self.assertEqual(inst.password, "")
        self.assertTrue(hasattr(inst, "first_name"))
        self.assertEqual(inst.first_name, "")
        self.assertTrue(hasattr(inst, "last_name"))
        self.assertEqual(inst.last_name, "")
