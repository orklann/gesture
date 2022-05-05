import unittest
from gesture.server import Server
from .dummy import DummyJob

class TestServer(unittest.TestCase):
    def test_fetch(self):
        server = Server()
        jobs = server.fetch()
