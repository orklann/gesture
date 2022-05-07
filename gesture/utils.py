import time

def normalize_item(item):
    # `created_at` is the key to make two same jobs different, so in general
    # we have two same jobs in Redis.
    item["created_at"] = time.time()
    return item
