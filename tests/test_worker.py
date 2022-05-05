import unittest
from gesture.worker import Worker
from .dummy import DummyJob

class TestWorker(unittest.TestCase):
    def test_start(self):
        job_str = '{"class": "DummyJob", "args": [1, 2, 3], "at": 12345}'
        worker = Worker()
        worker.run(job_str)
    
    def test_resolve_job(self):
        job_str = '{"class": "DummyJob", "args": [1, 2, 3], "at": 12345}'
        worker = Worker()
        instance, args = worker.resolve_job(job_str)
        self.assertTrue(type(instance) is DummyJob)
        self.assertEqual(args, [1, 2, 3])
