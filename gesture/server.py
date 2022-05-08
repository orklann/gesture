import time
import redis
from .worker import Worker

class Server:
    def __init__(self):
        self.redis = redis.Redis()
        self.worker = Worker()

    def start(self):
        while True:
            job_str = self.fetch()
            if job_str is not None:
                self.worker.run(job_str)
            time.sleep(0.1)
        
    def fetch(self):
        job = self.zpopbyscrore()
        if job is not None:
            return job.decode("utf-8")
        else:
            return None

    def zpopbyscrore(self):
        now = time.time()
        jobs = self.redis.zrangebyscore("schedule", min="-inf", max=now, start=0, num=1)
        if len(jobs) > 0:
            self.redis.zrem("schedule", jobs[0])
            return jobs[0]
        return None
