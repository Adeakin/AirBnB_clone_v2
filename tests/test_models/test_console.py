#!/usr/bin/python3
"""
Unittest for console.py
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for console.py"""

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd("create State name=\"California\"")
            self.assertTrue(fake_out.getvalue().strip().startswith("("))

    def test_create_with_multiple_params(self):
        """Test create command with multiple parameters"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd("create Place city_id=\"0001\" user_id=\"0001\" name=\"My_little_house\" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297")
            self.assertTrue(fake_out.getvalue().strip().startswith("[["))


if __name__ == '__main__':
    unittest.main()
