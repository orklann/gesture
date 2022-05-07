import time
import redis
from .worker import Worker

class Server:
    def __init__(self):
        self.redis = redis.Redis()
        self.worker = Worker()

    def start(self):
        print("Gesture server starts...")
        job_str = self.fetch()
        return self.worker.run(job_str)
        
    def fetch(self):
        jobs = self.redis.zrange("schedule", 0, 0)
        return jobs[0].decode("utf-8")

    def zpopbyscrore(self):
        now = time.time()
        jobs = self.redis.zrangebyscore("schedule", min="-inf", max=now, start=0, num=1)
        if jobs[0]:
            self.redis.zrem("schedule", jobs[0])
            return jobs[0]
        return None
