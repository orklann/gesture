import redis
import json
import time

class Client:
    def __init__(self):
        self.redis = redis.Redis()

    def _atomic_push(self, payloads):
        if "at" in payloads:
            time_stamp = payloads["at"]
            del payloads["at"]
            self.redis.zadd("schedule", {json.dumps(payloads): time_stamp})
