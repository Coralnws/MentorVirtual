# test_mentorvirtual.py
"""
Tests for MentorVirtual module.
"""

import unittest
from mentorvirtual import MentorVirtual

class TestMentorVirtual(unittest.TestCase):
    """Test cases for MentorVirtual class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MentorVirtual()
        self.assertIsInstance(instance, MentorVirtual)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MentorVirtual()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
