#!/usr/bin/python3
"""Test the checker."""

import unittest
from os import sys

sys.path.append('src')
sys.path.append('../src')

from checker import Checker


class TestChecker(unittest.TestCase):
    """Test the checker."""

    def test_exercise_success(self):
        """Dummy test."""
        self.maxDiff = None

        checker = Checker('tests/example_job.yml')
        results = checker.check_homework()
        self.assertEqual(len(results), 5)
        self.assertEqual(len(results['Exercise 1']), 2)
        self.assertEqual(results['Exercise 1']['Test 1'].stderr, "")
        self.assertTrue(results['Exercise 1']['Test 1'].succeeded())
        self.assertTrue(results['Exercise 1']['Test 2'].succeeded())

        self.assertEqual(len(results['Exercise 2']), 1)
        self.assertNotIn("Test 1", results['Exercise 2'])
        self.assertIn("Build Failed", results['Exercise 2'])

        self.assertTrue(results['Exercise 3']['Test 1'].succeeded())
        self.assertFalse(results['Exercise 3']['Test 2'].succeeded())

        self.assertTrue(results['Exercise 4']['Test 1'].succeeded())
        self.assertFalse(results['Exercise 4']['Test 2'].succeeded())
