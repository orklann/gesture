import unittest
from gesture.job import Job, NoClassError
from .dummy import DummyJob

class TestJob(unittest.TestCase):
    def test_perform_async(self):
        Job.perform_async(1, 2, 3)

    def test_class_by_name(self):
        klass = Job.class_by_name("DummyJob")
        self.assertEqual(klass is DummyJob, True)
        self.assertRaises(NoClassError, Job.class_by_name, "SomeJob")
