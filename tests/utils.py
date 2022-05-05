def clear_queue(redis, queue):
    redis.zremrangebyscore(queue, 0, 99999999999999)

