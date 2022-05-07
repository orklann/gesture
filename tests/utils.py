def clear_set(redis, set_name):
    redis.zremrangebyscore(set_name, 0, 99999999999999)

def clear_list(redis, list_name):
    redis.delete(list_name)
