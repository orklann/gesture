import unittest
from gesture.utils import *
from .dummy import DummyJob
import time

class TestUtils(unittest.TestCase):
    def test_validate(self):
        job = {"class": "DummyJob", 'args': [1]}
        validate(job)
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

    def test_safe_thread(self):
        def function():
            raise Exception("Dummy Exception!")

        thread = safe_thread(function)
        self.assertRaises(Exception, thread.join)
