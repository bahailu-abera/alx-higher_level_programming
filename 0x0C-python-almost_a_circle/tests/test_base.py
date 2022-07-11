#!/usr/bin/python3
""" Module for test Base class """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest import TestCase
from unittest.mock import Pach

class TestBaseMethods(TestCase):
    """ suite to test Base Class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0
