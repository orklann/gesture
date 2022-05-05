import unittest
from gesture.server import Server
from .dummy import DummyJob

class TestServer(unittest.TestCase):
    def test_fetch(self):
        server = Server()
        jobs = server.fetch()

    def test_start(self):
        server = Server()
        # clear all jobs before testing
        server.redis.zremrangebyscore("schedule", 0, 99999999999999)
        DummyJob.perform_async(100)
        result = server.start()
        self.assertEqual(result, 100)
