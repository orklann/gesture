import unittest
from gesture.worker import Worker
from .dummy import DummyJob

class TestWorker(unittest.TestCase):
    def test_run(self):
        job_str = '{"class": "DummyJob", "args": [1], "at": 12345}'
        worker = Worker()
        result = worker.run(job_str)
        self.assertEqual(result, 1)
    
    def test_resolve_job(self):
        job_str = '{"class": "DummyJob", "args": [1], "at": 12345}'
        worker = Worker()
        instance, args = worker.resolve_job(job_str)
        self.assertTrue(type(instance) is DummyJob)
        self.assertEqual(args, [1])

    def test_execute_job(self):
        job_str = '{"class": "DummyJob", "args": [1], "at": 12345}'
        worker = Worker()
        instance, args = worker.resolve_job(job_str)
        result = worker.execute_job(instance, args)
        self.assertEqual(result, 1)

        # Test DummyArgsJob
        job_str = '{"class": "DummyArgsJob", "args": [1, 2, 3], "at": 22222}'
        worker = Worker()
        instance, args = worker.resolve_job(job_str)
        result = worker.execute_job(instance, args)
        self.assertEqual(result, (1, 2, 3))
