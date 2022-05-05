import redis
import json
import time

class Client:
    def __init__(self):
        self.redis = redis.Redis()

    def push(self, payloads):
        return self._atomic_push(payloads)

    def _atomic_push(self, payloads):
        if "at" in payloads:
            time_stamp = payloads["at"]
            return self.redis.zadd("schedule", {json.dumps(payloads): time_stamp})
