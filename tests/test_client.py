import time
import unittest
from gesture.client import Client

class TestClient(unittest.TestCase):
    def test_atomic_push(self):
        client = Client()
        payloads = {"class": "DummyJob", "args": [1], "at": time.time()}
        job = client._atomic_push(payloads)
        self.assertEqual(job, 1)

    def test_push(self):
        client = Client()
        payloads = {"class": "DummyJob", "args": [1], "at": time.time()}
        job = client.push(payloads)
        self.assertEqual(job, 1)
        # Test pushing the same job, but with different time stamp
        payloads = {"class": "DummyJob", "args": [1], "at": time.time()}
        job = client.push(payloads)
        self.assertEqual(job, 1)
