import unittest
from gesture.server import Server
from .dummy import DummyJob
from .utils import clear_queue

class TestServer(unittest.TestCase):
    def test_fetch(self):
        server = Server()
        jobs = server.fetch()

    def test_start(self):
        server = Server()
        # clear all jobs before testing
        clear_queue(server.redis, "schedule")
        DummyJob.perform_async(100)
        result = server.start()
        self.assertEqual(result, 100)
