import time

def normalize_item(item):
    # `created_at` is the key to make two same jobs different, so normally
    # we have two same jobs in Redis.
    item["created_at"] = time.time()
    return item
