import unittest
from gesture.job import Job

class TestJob(unittest.TestCase):
    def test_perform_async(self):
        Job.perform_async(1, 2, 3)
