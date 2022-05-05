import unittest
from gesture.worker import Worker

class TestWorker(unittest.TestCase):
    def test_start(self):
        job_str = '{"class": "DummyJob", "args": [1, 2, 3], "at": 12345}'
        worker = Worker()
        worker.run(job_str)
