#!/usr/bin/python3
""" Module to test Square class """
import unittest
from models.square import Square

class TestSquareMethods(unittest.TestCase):
    """ Suit to test Square class """

    def setUp(self):
        """ Method executed after each test case """
        pass

    def test_size(self):
        """ Test the size """
        s = Square(4)
        self.assertEqual(s.size, 4)
