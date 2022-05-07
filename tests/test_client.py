import time
import unittest
from gesture.client import Client
from .utils import clear_set, clear_list

class TestClient(unittest.TestCase):
    def test_atomic_push(self):
        client = Client()
        clear_set(client.redis, "schedule")
        payloads = {"class": "DummyJob", "args": [1], "at": time.time()}
        job = client._atomic_push(payloads)
        self.assertEqual(job, 1)
        clear_list(client.redis, "queue")
        payloads = {"class": "DummyJob", "args": [2]}
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

        # Test pushing job without `at` key
        clear_list(client.redis, "queue")
        payloads = {"class": "DummyJob", "args": [1]}
        job = client.push(payloads)
        self.assertEqual(job, 1)
        # Sencod job
        payloads = {"class": "DummyJob", "args": [1]}
        job = client.push(payloads)
        self.assertEqual(job, 2)
