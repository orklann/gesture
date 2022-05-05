import time
from .client import Client

class Job:
    @classmethod
    def perform_async(cls, *args):
        payload = {"class": cls.__name__, "args": list(args)}
        payload["at"] = time.time()
        client = Client()
        client.push(payload)
        
