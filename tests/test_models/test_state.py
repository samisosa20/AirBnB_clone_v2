#!/usr/bin/python3
"""Contain tests for the state module."""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test the State class."""

    @classmethod
    def setUpClass(cls):
        cls.new_state = State()
        cls.new_state.name = "California"

    def test_State_inheritence(self):
        """Test that State class inherits"""
        self.assertIsInstance(self.new_state, BaseModel)

    def test_State_attributes(self):
        """Test that State class"""
        self.assertTrue("name" in self.new_state.__dir__())

    def test_State_attributes_type(self):
        """Test that State class"""
        self.assertIsInstance(self.new_state.name, str)
