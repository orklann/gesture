import redis
from .worker import Worker

class Server:
    def __init__(self):
        self.redis = redis.Redis()
        self.worker = Worker()

    def start(self):
        print("Gesture server starts...")
        job_str = self.fetch()
        self.worker.run(job_str)
        
    def fetch(self):
        jobs = self.redis.zrange("schedule", 0, 0)
        return jobs[0].decode("utf-8")
