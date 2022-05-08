import unittest
from gesture.utils import *
from .dummy import DummyJob

class TestUtils(unittest.TestCase):
    def test_validate(self):
        job = []
        self.assertRaises(ArgumentError, validate, job)
        job = {"args": [1], "at": 12345}
        self.assertRaises(ArgumentError, validate, job)
        job = {"class": "DummyJob", 'args': 1, "at": 12345.0}
        self.assertRaises(ArgumentError, validate, job)
        job = {"class": DummyJob, 'args': [1], "at": 12345.0}
        self.assertRaises(ArgumentError, validate, job)
        job = {"class": "DummyJob", 'args': [1], "at": 12345}
        self.assertRaises(ArgumentError, validate, job)
        job = {"class": "DummyJob", 'args': [1], "at": "12345.123"}
        self.assertRaises(ArgumentError, validate, job)
