import unittest
from gesture.client import Client

class TestClient(unittest.TestCase):
    def test_atomic_push(self):
        client = Client()
        payloads = {"class": "DummyJob", "args": [1, 2, 3], "at": 123}
        client._atomic_push(payloads)

